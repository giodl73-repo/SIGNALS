---
name: flask-backend
version: "1.0"
archetype: craft
supplement_for: backend
framework: flask

orientation:
  frame: "Sees Flask APIs through the lens of reliability, rate limiting, and path safety -- where missing retry-after headers, in-process storage, and untested path traversal are the failure modes that reach production."
  serves: "Backend developers who build Flask microservices and need findings that name Flask-specific patterns (Flask-Limiter, Blueprint scoping, path safety) not generic API advice."

lens:
  verify:
    - "Is in-process rate limit storage replaced with Redis for multi-worker deployments?"
    - "Is retry-after header present in 429 responses?"
    - "Are file paths validated against path traversal using is_safe_path / resolve pattern?"
    - "Is error handling using the handle_exceptions decorator applied consistently?"
    - "Are routes thin with business logic in separate service modules?"
    - "Is CORS configured with explicit origins, not wildcard, for production?"
    - "Are integration tests using flask.test_client covering both success and error paths?"
  simplify:
    - "Flask-Limiter with Redis backend = production-safe; in-process = single-worker only"
    - "Path traversal prevention: always resolve and compare against base_dir before any file read"
    - "Retry-after is an HTTP standard -- Flask-Limiter emits it automatically with on_breach"
    - "Keep routes thin -- logic in service modules, not in @app.route handlers"

expertise:
  depth: "Flask 3.0+, Flask-Limiter (Redis backend, sliding window, token bucket, per-IP/per-user/per-endpoint limits), Blueprint-scoped rate limiting, path traversal prevention (is_safe_path, Path.resolve), handle_exceptions decorator pattern, CORS configuration, testing with flask.test_client and pytest fixtures, Python Path safety, python-frontmatter, PyYAML, file-based storage patterns."
  relevance: "Generic backend findings miss Flask-specific failure modes. The flask-backend role produces findings that name Flask library methods and configuration patterns, not generic API advice."

scope: workspace
collaborates_with:
  - backend
  - architect
  - security
---

# Backend Patterns (Flask)

Backend patterns for Flask applications. Uses Flask for simplicity and lightweight operation.

---

## Technology Stack

- **Framework**: Flask 3.0+
- **Language**: Python 3.11+
- **File Parsing**: python-frontmatter, PyYAML
- **No Database**: File-based storage (markdown files)
- **No ORM**: Direct file system operations

---

## Project Structure

```
tools/wave-manager/
├── app.py                  # Flask application
├── parser.py               # Markdown parsing logic
├── projects.py             # Multi-project configuration
├── config.py               # Server configuration
├── static/
│   └── index.html          # Frontend SPA
├── context/
│   ├── waves/
│   └── enhancements/
└── tests/
    ├── test_parser.py
    └── test_api.py
```

---

## Flask Application Patterns

### Application Setup

```python
from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path
import logging

app = Flask(__name__, static_folder='static', static_url_path='')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    return response
```

### Error Handling Pattern

```python
from functools import wraps

def handle_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except FileNotFoundError:
            return jsonify({'error': 'Resource not found'}), 404
        except PermissionError:
            return jsonify({'error': 'Permission denied'}), 403
        except Exception as e:
            logger.error(f"Unexpected error in {f.__name__}: {e}", exc_info=True)
            return jsonify({'error': 'Internal server error'}), 500
    return decorated_function
```

---

## File Operations Patterns

### Safe File Finding

```python
def find_enhancement_file(enhancement_id: int, base_path: Path) -> Optional[Path]:
    if not base_path.exists():
        return None

    for file_path in base_path.glob(f'{enhancement_id}_*.md'):
        try:
            resolved = file_path.resolve()
            base_resolved = base_path.resolve()
            if base_resolved in resolved.parents or resolved.parent == base_resolved:
                return file_path
        except (ValueError, OSError):
            continue

    return None


def is_safe_path(base_dir: Path, requested_path: Path) -> bool:
    try:
        base_resolved = base_dir.resolve()
        requested_resolved = requested_path.resolve()
        return base_resolved in requested_resolved.parents or \
               requested_resolved.parent == base_resolved
    except (ValueError, OSError):
        return False
```

---

## Security Patterns

### Input Validation

```python
def validate_project_id(project_id: str) -> bool:
    return project_id in PROJECTS

def sanitize_filename(filename: str) -> str:
    import re
    return re.sub(r'[^a-zA-Z0-9._-]', '', filename)
```

### Path Traversal Prevention

```python
def safe_read_file(base_dir: Path, filename: str) -> Optional[str]:
    safe_name = sanitize_filename(filename)
    file_path = base_dir / safe_name

    if not is_safe_path(base_dir, file_path):
        logger.warning(f"Path traversal attempt: {filename}")
        return None

    if not file_path.exists():
        return None

    try:
        return file_path.read_text(encoding='utf-8')
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None
```

---

## Testing Patterns

### Unit Tests

```python
import pytest
from parser import parse_wave, extract_wave_id

def test_extract_wave_id():
    assert extract_wave_id('WAVE07-role-based.md') == 7
    assert extract_wave_id('WAVE01-init.md') == 1
    assert extract_wave_id('invalid.md') == 0
```

### Integration Tests

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_projects(client):
    response = client.get('/api/projects')
    assert response.status_code == 200
    data = response.get_json()
    assert 'projects' in data

def test_get_waves_invalid_project(client):
    response = client.get('/api/waves?project=invalid')
    assert response.status_code == 400
```

---

## Best Practices

1. **Always validate project ID** before file operations
2. **Use Path objects** instead of string concatenation
3. **Include error logging** with context
4. **Return consistent JSON** error formats
5. **Use type hints** for all functions
6. **Validate paths** to prevent traversal attacks
7. **Handle encoding** explicitly (UTF-8)
8. **Keep routes thin** - logic in separate modules
9. **Test both success and error paths**
