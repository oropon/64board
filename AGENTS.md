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
```
64board/
├── backend/
│   ├── app/
│   │   ├── __init__.py          # Flask factory (create_app)
│   │   ├── models.py            # SQLAlchemy ORM models
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── ui.py            # Template routes
│   │   ├── services/
│   │   │   └── __init__.py
│   │   └── templates/
│   │       ├── base.html        # Base Jinja2 template
│   │       └── index.html       # Main page
│   ├── tests/                   # pytest test suite
│   ├── config.py                # Flask configuration
│   ├── wsgi.py                  # WSGI entry point
│   ├── requirements.txt         # Python dependencies
│   └── requirements-dev.txt     # Dev dependencies (pytest, mypy, etc.)
├── frontend/
│   ├── src/                     # TypeScript/SCSS source
│   └── public/                  # Static assets (images, etc.)
├── docs/
│   └── architecture_overview.md
├── AGENTS.md
├── README.md
└── LICENSE
```

**Note**: `backend/static/dist/` (Vite build output) is created after running `npm run build` and should be in `.gitignore`.

→ **Start by reading** [`docs/architecture_overview.md`](./docs/architecture_overview.md)

---

## How to Work

| Phase | Command / Notes |
|-------|-----------------|
| **Setup (Backend)** | `cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt` |
| **Setup (Frontend)** | `cd frontend && npm install` |
| **Tests (Backend)** | `cd backend && pytest tests/ --cov=app --cov-report=term-missing` |
| **Tests (Frontend)** | `cd frontend && npm test` (Vitest or similar) |
| **Lint / Type (Backend)** | `cd backend && mypy app/` |
| **Lint / Type (Frontend)** | `cd frontend && npm run type-check` |
| **Build (Frontend)** | `cd frontend && npm run build` → outputs to `backend/static/dist/` |
| **Run (Dev)** | Terminal 1: `cd frontend && npm run dev` (port 5173)<br>Terminal 2: `cd backend && flask run` (port 5000) |
| **Run (Prod)** | `cd backend && flask run` (serves pre-built static assets) |

---

## Performance Budgets

| Target Device | Raspberry Pi Zero 2 W |
|----------------|----------------------|
| CPU | Quad-core 1 GHz Cortex-A53 |
| RAM | 512 MB |
| OS | Raspberry Pi OS Bookworm (64-bit) |
| Expected runtime | < 120 MB RAM usage / < 15 % CPU idle load |
| Build behavior | Vite dev mode HMR < 100 ms / Production build ≤ 10 s |

The entire application must stay responsive under these limits.

---

## Module Notes

### Backend (`backend/app/`)
- **`__init__.py`** – Flask application factory (`create_app()`)
- **`models.py`** – SQLite ORM models (SQLAlchemy 2.x)
- **`routes/ui.py`** – HTML template routes (render_template)
- **`routes/api.py`** – JSON API endpoints (REST) *(to be implemented)*
- **`services/pixoo.py`** – HTTP API client for Pixoo 64 local protocol *(to be implemented)*
- **`services/fonts.py`** – BMFont rendering using bmfontify library *(to be implemented)*
- **`services/jobs.py`** – Background job queue via ThreadPoolExecutor *(to be implemented)*
- **`templates/`** – Jinja2 templates (base.html, index.html)

### Frontend (`frontend/src/`)
- **`main.ts`** – TypeScript entry point
- **`styles/`** – SCSS stylesheets (Tabler UI integration)
- Vite builds to `backend/static/dist/` for Flask to serve

### Configuration
- **`backend/config.py`** – Flask configuration classes (dev/prod)
- **`backend/wsgi.py`** – WSGI entry point for production servers
- **`frontend/vite.config.ts`** – Vite build settings, proxy to Flask API

