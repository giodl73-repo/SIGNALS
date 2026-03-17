---
supplement_for: backend
framework: fastapi
---

# Backend Patterns (FastAPI)

This document defines backend coding patterns and best practices for FastAPI applications in the monorepo.

---

## Project Structure

```
<app>-backend/
├── app/
│   ├── main.py                 # FastAPI app
│   ├── config.py               # Settings
│   ├── database.py             # DB connection
│   ├── api/
│   │   ├── routes/             # Endpoints
│   │   └── deps.py             # Dependencies
│   ├── models/                 # SQLAlchemy models
│   ├── schemas/                # Pydantic schemas
│   └── services/               # Business logic
```

---

## Application Initialization

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import cards, stats
from app.database import engine, Base

# Create tables (development only)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TCM API",
    description="Trading Card Management API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cards.router, prefix="/api/cards", tags=["cards"])
app.include_router(stats.router, prefix="/api/stats", tags=["stats"])

@app.get("/api/health")
async def health():
    return {"status": "healthy"}
```

---

## Configuration

```python
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:pass@localhost:5432/db"
    secret_key: str = "dev-secret-key"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
```

---

## Database Connection

```python
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency for getting DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## Models (SQLAlchemy)

```python
# app/models/card.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    player = Column(String, index=True)
    team = Column(String)
    year = Column(Integer, index=True)
    value = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

---

## Schemas (Pydantic)

```python
# app/schemas/card.py
from pydantic import BaseModel, Field
from datetime import datetime

class CardBase(BaseModel):
    """Shared properties"""
    name: str = Field(..., min_length=1, max_length=200)
    player: str | None = None
    team: str | None = None
    year: int | None = Field(None, ge=1900, le=2100)
    value: float | None = Field(None, ge=0)

class CardCreate(CardBase):
    """Properties to receive on creation"""
    pass

class CardUpdate(CardBase):
    """Properties to receive on update"""
    name: str | None = None  # All fields optional for update

class Card(CardBase):
    """Properties to return to client"""
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility
```

---

## Services (Business Logic)

```python
# app/services/card_service.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.card import Card
from app.schemas.card import CardCreate, CardUpdate

class CardService:
    """Business logic for cards"""

    async def get(self, db: Session, id: int) -> Card | None:
        result = db.execute(select(Card).where(Card.id == id))
        return result.scalar_one_or_none()

    async def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> list[Card]:
        result = db.execute(select(Card).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, db: Session, obj_in: CardCreate) -> Card:
        db_obj = Card(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def update(self, db: Session, db_obj: Card, obj_in: CardUpdate) -> Card:
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def delete(self, db: Session, id: int) -> Card:
        obj = await self.get(db, id)
        db.delete(obj)
        db.commit()
        return obj

card_service = CardService()
```

---

## API Routes

```python
# app/api/routes/cards.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.card import Card, CardCreate, CardUpdate
from app.services.card_service import card_service

router = APIRouter()

@router.get("", response_model=list[Card])
async def get_cards(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    return await card_service.get_multi(db, skip=skip, limit=limit)

@router.get("/{card_id}", response_model=Card)
async def get_card(card_id: int, db: Session = Depends(get_db)):
    card = await card_service.get(db, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@router.post("", response_model=Card, status_code=201)
async def create_card(card_in: CardCreate, db: Session = Depends(get_db)):
    return await card_service.create(db, card_in)

@router.patch("/{card_id}", response_model=Card)
async def update_card(card_id: int, card_in: CardUpdate, db: Session = Depends(get_db)):
    card = await card_service.get(db, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return await card_service.update(db, card, card_in)

@router.delete("/{card_id}", response_model=Card)
async def delete_card(card_id: int, db: Session = Depends(get_db)):
    return await card_service.delete(db, card_id)
```

---

## Testing Patterns

```python
# tests/test_cards.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_cards():
    response = client.get("/api/cards")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_card():
    card_data = {
        "name": "Test Card",
        "player": "Test Player",
        "value": 10.00
    }
    response = client.post("/api/cards", json=card_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Card"
```

---

## Important Guidelines

### Do's
- Use type hints everywhere
- Follow PEP 8
- Use async/await for I/O operations
- Use Pydantic for validation
- Keep routes thin, logic in services
- Use SQLAlchemy ORM (no raw SQL)

### Don'ts
- Don't use `pip` - use `poetry` for Python packages
- Don't create database connections directly - use the session from `database.py`
- Don't write inline SQL - use SQLAlchemy
- Don't skip migrations when changing models
