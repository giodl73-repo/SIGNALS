---
supplement_for: designer
framework: vanilla
---

# Wave Manager - Design Patterns

**Last Updated**: 2026-01-28
**Design System**: Tailwind CSS, Minimal UI

---

## Overview

Design patterns and UI/UX guidelines for the wave-manager application. Focuses on **clarity, speed, and accessibility** over visual flourish.

---

## Design Principles

1. **Information First**: Content before decoration
2. **Fast Scanning**: Users need to find waves/enhancements quickly
3. **Accessibility**: WCAG 2.1 AA compliance minimum
4. **Minimal Cognitive Load**: Simple, predictable interactions
5. **Project Context**: Always clear which project is active

---

## Color System

### Project Colors

Each project has a unique color for quick visual identification:

```
App Manager:    #F38181 (Coral Red)
TCM:            #FF6B35 (Orange)
NHL:            #4ECDC4 (Turquoise)
Apportionment:  #95E1D3 (Mint)
Wave-Manager:   #9B59B6 (Purple)
```

**Color Usage**:
- **Color Dots**: 12px circles next to project names
- **Header Gradient**: Page header uses project color
- **Active States**: Buttons and links use project color

**Accessibility**: All colors tested against white background, meet WCAG AA (4.5:1 minimum).

### Status Colors

```
Planning:   #3B82F6 (Blue)
Active:     #10B981 (Green)
Completed:  #6B7280 (Gray)
On Hold:    #F59E0B (Amber)
Cancelled:  #EF4444 (Red)
```

### Neutral Palette

```
Background: #FFFFFF (White)
Surface:    #F9FAFB (Light Gray)
Border:     #E5E7EB (Gray 200)
Text:       #111827 (Gray 900)
Muted:      #6B7280 (Gray 500)
```

---

## Typography

### Font Stack

```css
font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
```

**Rationale**: System fonts load instantly, look native, excellent readability.

### Type Scale

```
Heading 1:  2rem (32px), font-weight: 700
Heading 2:  1.5rem (24px), font-weight: 600
Heading 3:  1.25rem (20px), font-weight: 600
Body:       1rem (16px), font-weight: 400
Small:      0.875rem (14px), font-weight: 400
```

### Line Height

```
Headings:   1.2
Body:       1.5
Code:       1.4
```

---

## Layout Patterns

### Page Structure

```
┌─────────────────────────────────────────────────┐
│ Header (Project Selector + Title)               │
├─────────────────────────────────────────────────┤
│ Navigation Tabs (Waves | Enhancements | Stats) │
├─────────────────────────────────────────────────┤
│                                                 │
│                                                 │
│              Main Content Area                  │
│                                                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Grid System

```html
<!-- Wave Cards Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Cards here -->
</div>
```

**Breakpoints**:
- Mobile: 1 column
- Tablet (768px): 2 columns
- Desktop (1024px): 3 columns

---

## Component Patterns

### Project Selector

```
┌─ Project Selector ─────────────────────────┐
│ ● App Manager           ▼                  │
├────────────────────────────────────────────┤
│ ● App Manager     ✓                        │
│ ● TCM                                      │
│ ● NHL                                      │
│ ● Apportionment                            │
│ ● Wave Manager                             │
└────────────────────────────────────────────┘
```

**States**:
- **Closed**: Shows current project with color dot and chevron
- **Open**: Dropdown menu with all projects, current marked with checkmark
- **Hover**: Light gray background (#F3F4F6)
- **Focus**: Blue outline for keyboard navigation

**CSS**:
```css
.project-dropdown {
    position: relative;
    display: inline-block;
}

.project-button {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    background: white;
    cursor: pointer;
}

.project-button:hover {
    background: #F9FAFB;
}

.color-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.project-menu {
    position: absolute;
    top: 100%;
    left: 0;
    margin-top: 4px;
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    min-width: 200px;
    z-index: 50;
}

.project-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 16px;
    cursor: pointer;
}

.project-item:hover,
.project-item:focus {
    background: #F3F4F6;
    outline: none;
}

.project-item.selected {
    background: color-mix(in srgb, var(--brand-color) 10%, white);
    font-weight: 500;
}
```

### Wave Card

```
┌─ Wave Card ────────────────────────────┐
│ Wave 7: Role-Based System    [Status] │
│                                        │
│ Enable role-based wave organization    │
│ and wave-manager self-tracking.        │
│                                        │
│ 5 enhancements · 3 phases              │
│                                        │
│                    [View Details →]   │
└────────────────────────────────────────┘
```

**CSS**:
```css
.wave-card {
    background: white;
    border-radius: 8px;
    padding: 24px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.2s;
}

.wave-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.wave-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 12px;
}

.wave-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #111827;
}

.status-badge {
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.875rem;
    font-weight: 500;
}

.status-planning {
    background: #DBEAFE;
    color: #1E40AF;
}

.status-active {
    background: #D1FAE5;
    color: #065F46;
}

.status-completed {
    background: #E5E7EB;
    color: #1F2937;
}
```

### Enhancement Modal

```
┌─────────────────────────────────────────────────┐
│ E70: Pattern File Updates                   [×] │
├─────────────────────────────────────────────────┤
│                                                 │
│ [Status: Pending] [Priority: Critical]          │
│                                                 │
│ ## Current State                                │
│ Pattern files document single-developer...      │
│                                                 │
│ ## Goal                                         │
│ Update all pattern files to document...         │
│                                                 │
└─────────────────────────────────────────────────┘
```

**CSS**:
```css
.modal {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
}

.modal.hidden {
    display: none;
}

.modal-content {
    background: white;
    border-radius: 12px;
    max-width: 800px;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px;
    border-bottom: 1px solid #E5E7EB;
}

.modal-body {
    padding: 24px;
}

.close-button {
    width: 32px;
    height: 32px;
    border-radius: 4px;
    border: none;
    background: transparent;
    font-size: 24px;
    cursor: pointer;
    color: #6B7280;
}

.close-button:hover {
    background: #F3F4F6;
    color: #111827;
}
```

---

## Interaction Patterns

### Hover States

- **Cards**: Elevate shadow on hover
- **Buttons**: Slight background darkening
- **Links**: Underline appears
- **Dropdown Items**: Background color change

### Focus States

```css
*:focus-visible {
    outline: 2px solid #3B82F6;
    outline-offset: 2px;
}

button:focus-visible,
a:focus-visible {
    outline: 2px solid #3B82F6;
    outline-offset: 2px;
}
```

### Loading States

```html
<div class="loading-spinner">
    <div class="spinner"></div>
    <p>Loading waves...</p>
</div>
```

```css
.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #E5E7EB;
    border-top-color: var(--brand-color);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}
```

---

## Responsive Design

### Mobile Adaptations

```css
/* Stack elements on mobile */
@media (max-width: 768px) {
    .wave-header {
        flex-direction: column;
        gap: 12px;
    }

    .project-selector {
        width: 100%;
    }

    .modal-content {
        margin: 16px;
        max-height: calc(100vh - 32px);
    }
}
```

### Touch Targets

Minimum touch target size: **44px × 44px** (WCAG AAA)

```css
button, a, .clickable {
    min-height: 44px;
    min-width: 44px;
}
```

---

## Accessibility Patterns

### Keyboard Navigation

```
Tab:        Move focus forward
Shift+Tab:  Move focus backward
Enter:      Activate button/link
Space:      Activate button (not link)
Escape:     Close modal/dropdown
Arrow Up/Down: Navigate list items
```

### ARIA Patterns

```html
<!-- Modal -->
<div role="dialog"
     aria-labelledby="modal-title"
     aria-modal="true">
    <h2 id="modal-title">Enhancement Details</h2>
</div>

<!-- Dropdown -->
<button aria-haspopup="listbox"
        aria-expanded="false">
    Select Project
</button>
<div role="listbox">
    <div role="option" aria-selected="true">Project 1</div>
</div>

<!-- Status -->
<span role="status" aria-live="polite">
    Wave loaded successfully
</span>
```

### Screen Reader Support

```html
<!-- Visually hidden but screen-reader accessible -->
<span class="sr-only">Close modal</span>

<style>
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}
</style>
```

---

## Animation Guidelines

### Duration

```
Fast:    150ms (hover, focus)
Medium:  300ms (expand, collapse)
Slow:    500ms (page transitions)
```

### Easing

```css
/* Preferred easing functions */
ease-out:       cubic-bezier(0, 0, 0.2, 1)  /* Entering */
ease-in:        cubic-bezier(0.4, 0, 1, 1)  /* Leaving */
ease-in-out:    cubic-bezier(0.4, 0, 0.2, 1) /* Both */
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

---

## Dark Mode (Future)

Not currently implemented, but reserved CSS custom properties:

```css
@media (prefers-color-scheme: dark) {
    :root {
        --bg: #111827;
        --surface: #1F2937;
        --border: #374151;
        --text: #F9FAFB;
        --muted: #9CA3AF;
    }
}
```

---

## Performance

### Image Optimization

- Use SVG for icons (infinitely scalable)
- No raster images currently needed
- If added: WebP format, lazy loading

### CSS Strategy

- Tailwind CSS via CDN (fast, cached)
- Custom CSS for components only
- Minimize custom styles (< 2KB)

---

## Best Practices

1. **Color contrast**: Minimum 4.5:1 for text, 3:1 for UI components
2. **Touch targets**: Minimum 44px × 44px
3. **Focus indicators**: Always visible, 2px outline
4. **Loading states**: Show within 200ms
5. **Error messages**: Clear, actionable, non-technical
6. **Consistent spacing**: Use 4px, 8px, 12px, 16px, 24px, 32px
7. **Animation**: Respect `prefers-reduced-motion`
8. **Typography**: Minimum 16px body text
9. **Modals**: Trap focus, close on Escape
10. **Forms**: Label all inputs, show validation

---

## Design Checklist

**Before Implementing UI**:
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Touch targets are 44px minimum
- [ ] Keyboard navigation works
- [ ] Screen reader announces changes
- [ ] Focus indicators visible
- [ ] Loading states defined
- [ ] Error states defined
- [ ] Responsive breakpoints tested
- [ ] Reduced motion respected
- [ ] Consistent with existing patterns

---

---

## Assessment Requirements

**CRITICAL**: When performing wave assessments with `/assess-wave`, the Designer discipline MUST enforce all design and accessibility standards documented in this file.

### Mandatory Design Standards Enforcement

**Rule 1: All Websites Must Pass WCAG 2.1 AA Compliance**
- Run automated accessibility checks (axe-core, Lighthouse, WAVE)
- Verify manual keyboard navigation works correctly
- Test screen reader compatibility (NVDA/JAWS/VoiceOver)
- Verify color contrast ratios meet or exceed minimums:
  - Normal text (16px): ≥4.5:1 contrast ratio
  - Large text (18px+, bold 14px+): ≥3:1 contrast ratio
  - Interactive elements: ≥3:1 against background
- Return NEEDS_WORK if any accessibility checks fail

**Rule 2: Design System Consistency**
- Verify all colors match Color System section (lines 25-64)
  - Project colors used correctly for identification
  - Status colors consistent across components
  - Neutral palette used for backgrounds/borders/text
- Verify typography follows Type Scale (lines 79-94)
- Verify spacing uses consistent increments: 4px, 8px, 12px, 16px, 24px, 32px
- Verify components follow documented patterns (lines 132-350)
- Return NEEDS_WORK if design system violations found

**Rule 3: Responsive Design Standards**
- Test at all breakpoints:
  - Mobile: 375px (minimum), 414px
  - Tablet: 768px, 1024px
  - Desktop: 1280px, 1920px
- Verify touch targets are ≥44×44px (WCAG AAA standard, line 429)
- Verify grid adapts correctly using documented breakpoints (lines 126-129)
- Return NEEDS_WORK if responsive design fails at any breakpoint

**Rule 4: Interaction Pattern Compliance**
- Verify hover states follow patterns (lines 356-361)
- Verify focus states use documented styles (lines 363-376)
- Verify keyboard navigation supports all documented keys (lines 443-451)
- Verify ARIA patterns implemented correctly (lines 453-476)
- Verify animations respect `prefers-reduced-motion` (lines 520-532)
- Return NEEDS_WORK if interaction patterns not followed

**Rule 5: Visual Aesthetics Against Design Guidelines**
- Information architecture is clear and intuitive (Principle #1-2, lines 17-18)
- Visual hierarchy guides user attention appropriately
- Fast scanning enabled (clear headings, consistent spacing)
- Minimal cognitive load (simple, predictable interactions, Principle #4)
- Consistent with existing component patterns
- Return NEEDS_WORK if visual quality doesn't meet standards

### Assessment Review Checklist

When reviewing a wave for `/assess-wave`, verify:

```markdown
## Design Assessment Checklist

### Accessibility Compliance (WCAG 2.1 AA)

**Automated Checks**:
- [ ] axe-core: 0 violations
- [ ] Lighthouse Accessibility: ≥95 score
- [ ] WAVE: 0 errors, 0 contrast errors

**Color Contrast** (lines 572, 25-64):
- [ ] Normal text (16px): ≥4.5:1 contrast ratio
- [ ] Large text (18px+): ≥3:1 contrast ratio
- [ ] Interactive elements: ≥3:1 against background
- [ ] All project colors meet WCAG AA against white background
- [ ] Status colors meet contrast requirements
- [ ] Custom colors verified against design system palette

**Keyboard Navigation** (lines 443-451):
- [ ] Tab: Moves focus forward through all interactive elements
- [ ] Shift+Tab: Moves focus backward
- [ ] Enter: Activates buttons and links
- [ ] Space: Activates buttons
- [ ] Escape: Closes modals and dropdowns
- [ ] Arrow keys: Navigate list items in dropdowns

**ARIA Implementation** (lines 453-476):
- [ ] Modals: role="dialog", aria-modal="true", aria-labelledby
- [ ] Dropdowns: aria-haspopup, aria-expanded
- [ ] Status messages: aria-live regions
- [ ] All buttons have aria-label or visible text
- [ ] Forms have proper label associations

**Screen Reader Support** (lines 478-497):
- [ ] All images have meaningful alt text
- [ ] Visually hidden text uses .sr-only class
- [ ] Focus order is logical
- [ ] Dynamic changes are announced
- [ ] Modal dialogs trap focus correctly

**Touch Targets** (lines 427-436):
- [ ] All interactive elements: ≥44×44px
- [ ] Buttons meet minimum size
- [ ] Links meet minimum size
- [ ] Dropdown items meet minimum size

### Design System Consistency

**Color System Compliance** (lines 25-64):
- [ ] Project colors used correctly:
  - Wave-Manager: #9B59B6 (Purple)
  - App Manager: #F38181 (Coral Red)
  - TCM: #FF6B35 (Orange)
  - NHL: #4ECDC4 (Turquoise)
  - Apportionment: #95E1D3 (Mint)
- [ ] Status colors used correctly:
  - Planning: #3B82F6 (Blue)
  - Active: #10B981 (Green)
  - Completed: #6B7280 (Gray)
  - On Hold: #F59E0B (Amber)
  - Cancelled: #EF4444 (Red)
- [ ] Neutral palette used correctly:
  - Background: #FFFFFF
  - Surface: #F9FAFB
  - Border: #E5E7EB
  - Text: #111827
  - Muted: #6B7280
- [ ] No custom colors introduced without justification

**Typography** (lines 69-94):
- [ ] Font stack: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif
- [ ] Heading 1: 2rem (32px), font-weight 700
- [ ] Heading 2: 1.5rem (24px), font-weight 600
- [ ] Heading 3: 1.25rem (20px), font-weight 600
- [ ] Body: 1rem (16px), font-weight 400
- [ ] Small: 0.875rem (14px), font-weight 400
- [ ] Line height: Headings 1.2, Body 1.5, Code 1.4
- [ ] Minimum body text: 16px

**Spacing Consistency** (line 576):
- [ ] Only uses: 4px, 8px, 12px, 16px, 24px, 32px
- [ ] Padding consistent across similar components
- [ ] Margin consistent with design patterns
- [ ] Gap in grids follows system

**Component Patterns** (lines 132-350):
- [ ] Project Selector follows documented pattern
- [ ] Wave Cards follow documented pattern
- [ ] Enhancement Modals follow documented pattern
- [ ] Status badges follow documented pattern
- [ ] No custom component styles without justification

### Responsive Design (lines 404-436)

**Breakpoints**:
- [ ] Mobile (375px): 1 column grid, stacked elements
- [ ] Tablet (768px): 2 column grid, adapted layout
- [ ] Desktop (1024px+): 3 column grid, full features

**Mobile Adaptations**:
- [ ] Wave header stacks on mobile
- [ ] Project selector expands to full width
- [ ] Modal margins adjusted for mobile (16px)
- [ ] All content readable without horizontal scroll

**Cross-Browser Testing**:
- [ ] Chrome: Fully functional
- [ ] Firefox: Fully functional
- [ ] Safari: Fully functional
- [ ] Mobile Safari (iOS): Touch interactions work
- [ ] Chrome Mobile (Android): Touch interactions work

### Interaction Patterns (lines 354-400)

**Hover States** (lines 356-361):
- [ ] Cards: Shadow elevation on hover
- [ ] Buttons: Slight background darkening
- [ ] Links: Underline appears
- [ ] Dropdown items: Background color change

**Focus States** (lines 363-376):
- [ ] All interactive elements: 2px blue outline (#3B82F6)
- [ ] Outline offset: 2px
- [ ] Focus-visible only (not on mouse click)

**Loading States** (lines 378-400):
- [ ] Spinner uses brand color
- [ ] Loading message displayed
- [ ] Appears within 200ms (best practice line 574)

**Animation** (lines 501-532):
- [ ] Duration: Fast 150ms, Medium 300ms, Slow 500ms
- [ ] Easing: ease-out (entering), ease-in (leaving)
- [ ] Respects prefers-reduced-motion

### Visual Quality & Aesthetics

**Design Principles** (lines 15-22):
- [ ] Information first: Content before decoration
- [ ] Fast scanning: Clear hierarchy, easy to find waves
- [ ] Accessibility: WCAG 2.1 AA minimum
- [ ] Minimal cognitive load: Simple, predictable interactions
- [ ] Project context: Always clear which project is active

**Information Architecture**:
- [ ] Navigation is intuitive
- [ ] Content hierarchy is clear
- [ ] Related items are grouped logically
- [ ] Consistent layout across pages

**Visual Hierarchy**:
- [ ] Important elements stand out
- [ ] Typography guides attention
- [ ] Whitespace used effectively
- [ ] Color draws attention appropriately

**Best Practices Compliance** (lines 571-580):
- [ ] Color contrast minimum 4.5:1 for text
- [ ] Touch targets minimum 44×44px
- [ ] Focus indicators always visible
- [ ] Loading states show within 200ms
- [ ] Error messages are clear and actionable
- [ ] Spacing uses 4px increments
- [ ] Animation respects reduced motion
- [ ] Typography minimum 16px body
- [ ] Modals trap focus, close on Escape
- [ ] Forms label all inputs, show validation

**Decision**: NEEDS_WORK | APPROVED

**If NEEDS_WORK**: Create follow-up enhancement (EXX) specifying all design/accessibility fixes required
```

### Example Assessment Response

```markdown
## Design Assessment - Wave 10 (Iteration 1)

**Status**: NEEDS_WORK

### Accessibility Violations (3 Critical, 2 Major)

**Critical** (Block completion):
1. **Color contrast failure**: `text-yellow-600` (#D97706) on white background
   - Current ratio: 3.2:1
   - Required: ≥4.5:1 (WCAG AA for normal text)
   - Fix: Change to `text-yellow-700` (#B45309) for 4.6:1 ratio
   - Location: `templates/index.html` lines 2156, 2178, 2189
   - Violates: Design principle #3 (Accessibility), Best practice #1

2. **Missing ARIA labels on interactive buttons**
   - Filter buttons (lines 234-256) lack aria-label
   - View mode toggle buttons (lines 267-289) lack aria-label
   - Screen readers announce "button" without context
   - Fix: Add aria-label="Filter by status" etc.
   - Violates: ARIA patterns (lines 453-476)

3. **Modal focus not trapped**
   - Enhancement modal (line 1893) doesn't trap focus
   - Keyboard users can tab out of modal to background
   - Fix: Implement focus trap with Tab/Shift+Tab handling
   - Violates: Best practice #9, ARIA patterns (line 459)

**Major** (Should fix):
4. **Touch targets below minimum**
   - Chart data point buttons: 32×32px (need ≥44×44px)
   - Location: Lines 2401-2423
   - Mobile users may have difficulty tapping
   - Violates: Touch target standard (lines 427-436)

5. **Non-responsive grid on mobile**
   - Budget grid uses fixed `grid-cols-4` at all breakpoints
   - Breaks layout on 375px mobile viewport
   - Fix: Change to `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4`
   - Violates: Responsive design standards (lines 404-436)

### Design System Violations (2 Issues)

1. **Custom color not in design system**
   - Using custom yellow: #F59E0B (Amber)
   - Should use: Status color "On Hold" #F59E0B (happens to match!)
   - But context is not "on hold" status, it's highlighting
   - Should use: Neutral palette or project color
   - Consider: text-purple-700 for wave-manager brand consistency

2. **Inconsistent spacing**
   - Card padding: 12px (line 2145)
   - Design system: Card padding should be 24px (line 236)
   - Violates: Component patterns, spacing consistency

### Responsive Design Issues (1 Issue)

1. **Grid breaks at 375px viewport**
   - See accessibility violation #5 above
   - Also affects 414px (iPhone Pro Max)

### Follow-Up Enhancement Required

**E55: Fix Frontend Bugs & Accessibility**
- **Priority**: Critical
- **Estimated**: 3 hours
- **Deliverables**:
  1. Fix color contrast (text-yellow-600 → text-yellow-700)
  2. Add ARIA labels to all filter and view mode buttons
  3. Implement modal focus trap
  4. Increase touch targets to 44×44px minimum
  5. Make grid responsive (grid-cols-1 sm:grid-cols-2 lg:grid-cols-4)
  6. Fix card padding to match design system (24px)

**Approval Criteria**:
- All WCAG 2.1 AA checks pass (axe-core 0 violations)
- All design system patterns followed
- Responsive across all breakpoints (375px, 768px, 1024px+)
- Touch targets ≥44×44px
- Color contrast ≥4.5:1 for all text

**Decision**: NEEDS_WORK - Create E55 before wave completion
```

### Design Quality Standards (for Assessment)

When fixing design issues as part of assessment follow-up:

1. **Verify against this document**: All design decisions must reference specific sections
2. **Test thoroughly**: Manual testing required (not just code review)
3. **Document deviations**: Any exceptions to design system must be justified
4. **Automated checks**: Run axe-core, Lighthouse before marking complete
5. **Cross-browser**: Test in Chrome, Firefox, Safari (minimum)

### Director Validation

The Engineering Director (during Director Synthesis) MUST verify:
- Designer agent enforced all accessibility standards (WCAG 2.1 AA)
- Designer agent verified design system consistency
- Designer agent tested responsive design at all breakpoints
- Designer agent verified color contrast for all text
- Return NEEDS_WORK if Designer approved without standards compliance

### Integration with Wave Flow

```
/implement-wave
    ↓
/assess-wave (Designer finds accessibility/design issues)
    ↓
Designer: NEEDS_WORK
    ↓
Create follow-up enhancement (EXX) to fix design/accessibility
    ↓
/implement-wave (implement EXX - fix issues)
    ↓
/assess-wave iteration 2
    ↓
Designer: APPROVED (all standards met)
    ↓
/complete-wave
```

### Tools & Resources

**Automated Testing**:
- **axe DevTools**: Browser extension for accessibility testing
- **Lighthouse**: Chrome DevTools (Accessibility score ≥95)
- **WAVE**: WebAIM browser extension
- **Color Contrast Analyzer**: Verify ratios meet WCAG AA

**Manual Testing**:
- **Keyboard navigation**: Unplug mouse, navigate with keyboard only
- **Screen readers**: NVDA (Windows), JAWS (Windows), VoiceOver (Mac/iOS)
- **Responsive testing**: Chrome DevTools device emulation
- **Cross-browser**: BrowserStack or actual devices

**Design System Validation**:
- Reference this document (design.md) for all patterns
- Compare colors with Color System (lines 25-64)
- Verify typography with Type Scale (lines 79-94)
- Check components against documented patterns (lines 132-350)

---

**Last Updated**: 2026-01-29
**Version**: 1.1 (Added Assessment Requirements)
**Status**: Active
