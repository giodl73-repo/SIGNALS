---
name: vanilla-frontend
version: "1.0"
archetype: craft
supplement_for: frontend
framework: vanilla

orientation:
  frame: "Sees vanilla JS / Flask-template frontends through the lens of DOM safety, state consistency, and fetch error handling — where innerHTML without sanitization, project state not persisted to localStorage, and missing fetch error boundaries are the failure modes that reach production."
  serves: "Developers building wave-manager style apps with vanilla ES6+, Flask Jinja2 templates, and Tailwind CDN who need findings that name specific DOM safety violations and state management gaps without a framework abstraction layer."

lens:
  verify:
    - "Is all user-generated or API-returned HTML sanitized with DOMPurify before innerHTML?"
    - "Does every fetch() call have error handling with a user-visible error state?"
    - "Is project selection persisted to localStorage and read back on page load?"
    - "Are debounce functions used on search/filter operations to prevent API flooding?"
    - "Is the project API parameter included in all data fetch calls?"
    - "Are dynamic event listeners cleaned up to prevent memory leaks?"
    - "Does updateBranding() run whenever currentProject changes?"
  simplify:
    - "innerHTML without DOMPurify is an XSS vulnerability — flag it as critical, not cosmetic"
    - "fetch without error handling means silent failures — always verify catch paths"
    - "localStorage persistence is the vanilla equivalent of state management — always check it"
    - "Global state mutations need dedicated functions — flag direct assignment to shared variables"

expertise:
  depth: "Vanilla ES6+ patterns, Jinja2 templates, DOMPurify, localStorage state management, Tailwind CSS CDN, Marked.js markdown rendering, debounce patterns"
  relevance: "High for any Flask-template frontend — no framework means all patterns are manual"

collaborates_with:
  - designer
  - testing
  - backend
---

# Wave Manager - Frontend Patterns

**Last Updated**: 2026-01-28
**Technology**: Vanilla JavaScript, Flask Templates, Tailwind CSS

---

## Overview

Frontend patterns for the wave-manager application. Unlike the main App Manager (React/TypeScript), wave-manager uses **vanilla JavaScript** with **Flask templates** for simplicity and fast iteration.

---

## Technology Stack

- **Templating**: Flask Jinja2 templates
- **JavaScript**: Vanilla ES6+ (no frameworks)
- **Styling**: Tailwind CSS (CDN)
- **Markdown**: Marked.js (CDN)
- **Sanitization**: DOMPurify (CDN)

---

## Component Patterns

### Project Selector Component

```javascript
// State management
let currentProject = localStorage.getItem('selectedProject') || 'appmanager';
let projects = [];

// Load projects from API
async function initProjectSelector() {
    try {
        const response = await fetch('/api/projects');
        const data = await response.json();
        projects = data.projects || [];
        renderProjectSelector();

        // Check URL parameter
        const urlParams = new URLSearchParams(window.location.search);
        const projectParam = urlParams.get('project');
        if (projectParam && isValidProject(projectParam)) {
            switchProject(projectParam);
        }
    } catch (error) {
        console.error('Failed to load projects:', error);
    }
}

// Render dropdown
function renderProjectSelector() {
    const selector = document.getElementById('projectSelector');
    const current = projects.find(p => p.id === currentProject);

    selector.innerHTML = `
        <div class="project-dropdown">
            <button onclick="toggleProjectMenu()" aria-label="Select project">
                <span class="color-dot" style="background: ${current?.color}"></span>
                <span>${current?.name}</span>
            </button>
            <div class="project-menu hidden">
                ${projects.map(p => `
                    <div onclick="selectProject('${p.id}')"
                         class="${p.id === currentProject ? 'selected' : ''}">
                        <span class="color-dot" style="background: ${p.color}"></span>
                        <span>${p.name}</span>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function selectProject(projectId) {
    currentProject = projectId;
    localStorage.setItem('selectedProject', projectId);
    updateBranding();
    reloadData();
    closeProjectMenu();
}
```

### Wave Cards Display

```javascript
function renderWaves(waves) {
    const container = document.getElementById('wavesContainer');

    container.innerHTML = waves.map(wave => `
        <div class="wave-card" data-wave-id="${wave.id}">
            <div class="wave-header">
                <h3>Wave ${wave.id}: ${wave.title}</h3>
                <span class="status-badge status-${wave.status}">${wave.status}</span>
            </div>
            <p class="wave-description">${wave.description || ''}</p>
            <div class="wave-stats">
                <span>${wave.enhancements?.length || 0} enhancements</span>
                <span>${wave.phases?.length || 0} phases</span>
            </div>
            <button onclick="viewWave(${wave.id})" class="btn-primary">
                View Details
            </button>
        </div>
    `).join('');
}
```

### Enhancement Modal

```javascript
async function showEnhancement(enhancementId) {
    try {
        const response = await fetch(`/api/enhancements/${enhancementId}?project=${currentProject}`);
        const data = await response.json();

        const modal = document.getElementById('enhancementModal');
        const content = document.getElementById('modalContent');

        content.innerHTML = `
            <div class="modal-header">
                <h2>E${data.id}: ${data.title}</h2>
                <button onclick="closeModal()" aria-label="Close">&times;</button>
            </div>
            <div class="modal-body">
                <div class="metadata">
                    <span class="status">${data.status}</span>
                    <span class="priority">${data.priority}</span>
                </div>
                <div class="markdown-content">
                    ${renderMarkdown(data.content)}
                </div>
            </div>
        `;

        modal.classList.remove('hidden');
        modal.setAttribute('aria-hidden', 'false');
    } catch (error) {
        showError('Failed to load enhancement');
    }
}

function closeModal() {
    const modal = document.getElementById('enhancementModal');
    modal.classList.add('hidden');
    modal.setAttribute('aria-hidden', 'true');
}

// Close on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});
```

---

## API Integration Patterns

### Fetch with Project Context

```javascript
async function fetchWaves() {
    const response = await fetch(`/api/waves?project=${currentProject}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
}

async function fetchEnhancements(waveId) {
    const url = `/api/enhancements?project=${currentProject}` +
                (waveId ? `&wave=${waveId}` : '');
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
}
```

### Error Handling

```javascript
async function loadWaves() {
    try {
        const data = await fetchWaves();
        waves = data.waves || [];
        renderWaves(waves);
    } catch (error) {
        console.error('Failed to load waves:', error);
        waves = [];
        showError('Unable to load waves. Please refresh.');
        renderWaves([]); // Show empty state
    }
}

function showError(message) {
    const toast = document.createElement('div');
    toast.className = 'error-toast';
    toast.textContent = message;
    toast.setAttribute('role', 'alert');
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 5000);
}
```

---

## Styling Patterns

### Tailwind Utility Classes

```html
<!-- Wave Card -->
<div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
    <h3 class="text-xl font-semibold text-gray-800 mb-2">Wave Title</h3>
    <p class="text-gray-600 mb-4">Description</p>
    <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
        View Details
    </button>
</div>

<!-- Status Badge -->
<span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium
             bg-green-100 text-green-800">
    Completed
</span>
```

### Dynamic Theming

```javascript
function updateBranding() {
    const project = projects.find(p => p.id === currentProject);
    if (!project) return;

    // Update CSS custom property
    document.documentElement.style.setProperty('--brand-color', project.color);

    // Update page title
    document.title = `${project.name} - Wave Manager`;
}
```

```css
:root {
    --brand-color: #F38181;
}

.header-bar {
    background: linear-gradient(135deg, var(--brand-color), color-mix(in srgb, var(--brand-color) 80%, black));
}
```

---

## Markdown Rendering

### Safe Markdown Parsing

```javascript
function renderMarkdown(text) {
    if (!text) return '';

    // Parse with Marked.js
    let html = marked.parse ? marked.parse(text) : marked(text);

    // Sanitize to prevent XSS
    if (typeof DOMPurify !== 'undefined') {
        html = DOMPurify.sanitize(html, {
            ALLOWED_TAGS: ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li',
                          'code', 'pre', 'a', 'strong', 'em', 'table',
                          'thead', 'tbody', 'tr', 'th', 'td', 'blockquote'],
            ALLOWED_ATTR: ['href', 'target', 'rel', 'class']
        });
    }

    return html;
}
```

---

## Accessibility Patterns

### Keyboard Navigation

```javascript
// Project dropdown keyboard support
function handleProjectKeydown(event, projectId) {
    switch (event.key) {
        case 'Enter':
        case ' ':
            event.preventDefault();
            selectProject(projectId);
            break;
        case 'Escape':
            closeProjectMenu();
            break;
        case 'ArrowDown':
            event.preventDefault();
            focusNextProject();
            break;
        case 'ArrowUp':
            event.preventDefault();
            focusPreviousProject();
            break;
    }
}
```

### ARIA Attributes

```html
<!-- Modal -->
<div id="modal"
     class="modal"
     role="dialog"
     aria-labelledby="modalTitle"
     aria-hidden="true">
    <h2 id="modalTitle">Enhancement Details</h2>
    <button aria-label="Close modal" onclick="closeModal()">×</button>
</div>

<!-- Dropdown -->
<button aria-haspopup="listbox"
        aria-expanded="false"
        onclick="toggleMenu()">
    Select Project
</button>
<div role="listbox" class="menu hidden">
    <div role="option" aria-selected="true">Project 1</div>
</div>
```

---

## State Management

### LocalStorage Persistence

```javascript
// Save user preferences
function savePreference(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
        console.warn('Failed to save preference:', e);
    }
}

function loadPreference(key, defaultValue) {
    try {
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : defaultValue;
    } catch (e) {
        return defaultValue;
    }
}

// Usage
const currentProject = loadPreference('selectedProject', 'appmanager');
const viewMode = loadPreference('viewMode', 'waves');
```

---

## Performance Patterns

### Debounce Search

```javascript
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func(...args), wait);
    };
}

const searchWaves = debounce((query) => {
    const filtered = waves.filter(w =>
        w.title.toLowerCase().includes(query.toLowerCase())
    );
    renderWaves(filtered);
}, 300);
```

### Lazy Loading

```javascript
// Load enhancement content only when modal opens
async function showEnhancement(id) {
    showLoadingSpinner();
    const data = await fetchEnhancement(id);
    hideLoadingSpinner();
    renderEnhancement(data);
}
```

---

## Testing Patterns

### Manual Testing Checklist

```
□ All projects load in selector
□ Switching projects updates UI correctly
□ Wave cards display all metadata
□ Enhancement modals open/close smoothly
□ Keyboard navigation works (Tab, Enter, Escape)
□ Screen reader announces state changes
□ Error messages display for failed requests
□ localStorage persists project selection
□ Markdown renders safely (no XSS)
□ Colors meet WCAG AA contrast (4.5:1)
```

---

## Best Practices

1. **Always sanitize markdown** before rendering to DOM
2. **Use fetch() with error handling** - never assume success
3. **Include project parameter** in all API calls
4. **Update URL on project switch** for deep linking
5. **Support keyboard navigation** for all interactive elements
6. **Provide ARIA labels** for screen readers
7. **Show loading states** during async operations
8. **Persist preferences** to localStorage
9. **Use debounce** for search/filter operations
10. **Keep JavaScript vanilla** - no framework dependencies

---

## Anti-Patterns to Avoid

❌ Don't use jQuery or other frameworks
❌ Don't mutate global state without dedicated functions
❌ Don't render user content without sanitization
❌ Don't ignore keyboard users
❌ Don't use `innerHTML` without DOMPurify
❌ Don't forget error handling on fetch
❌ Don't hardcode project IDs in UI code

---

**Last Updated**: 2026-01-28
**Version**: 1.0
**Status**: Active
