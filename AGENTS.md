# AGENTS.md

## Project: 64board
A self-hosted Flask-based web console for controlling **Pixoo 64 LED displays**.  
It allows uploading or generating images (including AI-generated ones), overlaying BMFont-rendered text, and scheduling automatic updates — all running locally on a Raspberry Pi Zero 2 W.

---

## Goals & Non-Goals

### Goals
- Provide a lightweight, browser-based management console for Pixoo 64 boards  
- Support BMFont text rendering and image overlay directly from the UI  
- Schedule periodic or on-demand display updates  
- Run entirely on a Raspberry Pi Zero 2 W
- Maintain clear, testable Python + TypeScript codebase (90% line / 80 % branch coverage)

### Non-Goals
- Full image-editing or animation suite  
- Cloud hosting, user accounts, or remote sync  
- Heavy front-end frameworks (React/Vue)  
- Real-time collaboration or multi-user control

---

## Project Layout
src/                # Application source
├─ app.py         # Flask entry / factory
├─ routes/        # UI & API blueprints
├─ services/      # Core logic (Pixoo, font, scheduler)
├─ static/        # Built JS/CSS
└─ templates/     # Jinja2 templates
docs/               # SDD / ADR design docs
tests/              # pytest test suite

→ **Start by reading** [`docs/architecture_overview.md`](./docs/architecture_overview.md)

---

## How to Work

| Phase | Command / Notes |
|-------|-----------------|
| **Setup** | TODO |
| **Tests** | TODO |
| **Lint / Type** | TODO |
| **Build** | `flask assets build` → bundles TS / SCSS via esbuild + libsass |
| **Run** | `flask run` (auto-watch for TS / SCSS rebuilds in dev mode) |

---

## Performance Budgets

| Target Device | Raspberry Pi Zero 2 W |
|----------------|----------------------|
| CPU | Quad-core 1 GHz Cortex-A53 |
| RAM | 512 MB |
| OS | Raspberry Pi OS Bookworm (64-bit) |
| Expected runtime | < 120 MB RAM usage / < 15 % CPU idle load |
| Build behavior | Local esbuild + libsass watch mode ≤ 3 s per update |

The entire application must stay responsive under these limits.

---

## Module Notes
- **`services/pixoo.py`** – HTTP API client for Pixoo 64 local protocol  
- WIP

