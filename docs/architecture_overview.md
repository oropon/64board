# Architecture Overview — 64board

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│  backend/app/                                       │
│  ├─ __init__.py         → Flask factory            │
│  ├─ routes/ui.py        → HTML templates (Jinja2)  │
│  ├─ routes/api.py       → REST JSON (TBD)          │
│  ├─ services/pixoo.py   → Pixoo 64 HTTP API (TBD)  │
│  ├─ services/fonts.py   → BMFont (bmfontify) (TBD) │
│  ├─ services/jobs.py    → ThreadPoolExecutor (TBD) │
│  ├─ models.py           → SQLite ORM models        │
│  └─ templates/          → Jinja2 templates         │
│       ├─ base.html                                 │
│       └─ index.html                                │
└─────────────────────────────────────────────────────┘
          │
          │ JSON / REST API
          ▼
┌─────────────────────────────────────────────────────┐
│  frontend/src/                                      │
│  ├─ main.ts             → TypeScript entry         │
│  └─ styles/             → SCSS (Tabler UI)         │
│                                                     │
│  Development: Vite dev server (port 5173)          │
│               ↓ proxies API to Flask (port 5000)   │
│                                                     │
│  Production:  npm run build                        │
│               ↓ outputs to backend/static/dist/    │
│               ↓ Flask serves static assets         │
└─────────────────────────────────────────────────────┘
```

---

## 2. Adopted Technologies

| Layer | Technology | Rationale |
|-------|-------------|------------|
| **Framework** | Flask 3.x | Lightweight, modular, simple to host on Pi |
| **Template Engine** | Jinja2 | Built-in, supports server-side composition |
| **UI Framework** | Tabler UI (Bootstrap 5) | Provides admin components with minimal weight |
| **Language** | TypeScript | Safer client scripting without frameworks |
| **CSS Preprocessor** | SCSS | Modern styling with Tabler UI integration |
| **Build Tool** | Vite + Node.js | Fast HMR, official TypeScript/SCSS support |
| **Database** | SQLite + SQLAlchemy 2.x | Zero-config persistence, small footprint |
| **Job Execution** | ThreadPoolExecutor | Simple background jobs; no Celery |
| **Testing (Backend)** | pytest + coverage | Lightweight and Pi-friendly |
| **Testing (Frontend)** | Vitest (or similar) | Vite-native test runner |

---

## 3. Design Principles

1. **Minimalism:** keep runtime dependencies small; Node.js used only for build-time tooling.
2. **Transparency:** architecture readable by humans & AI agents alike.
3. **Separation of concerns:** routes / services / UI clearly divided.
4. **Extendability:** new renderers or job types can be plugged in without restructuring.

---

## 4. Build and Runtime Flow

### Development Mode
1. **Terminal 1**: `cd frontend && npm run dev` starts Vite dev server (port 5173)
   - HMR enabled for instant TypeScript/SCSS updates
   - Proxies `/api/*` requests to Flask backend
2. **Terminal 2**: `cd backend && flask run` starts Flask (port 5000)
   - Serves Jinja2 templates (`templates/base.html`, `templates/index.html`)
   - Base template includes Vite dev server script tags for HMR
3. Access the app at `http://localhost:5000` (Flask serves HTML, Vite serves assets)

### Production Mode
1. **Build Frontend**: `cd frontend && npm run build`
   - Vite bundles TypeScript + SCSS → `backend/static/dist/`
   - Generates `manifest.json` for asset references
2. **Run Backend**: `cd backend && flask run`
   - Flask serves Jinja2 templates with references to built assets
   - No separate frontend server needed
3. Templates automatically switch from dev (Vite HMR) to prod (static assets) based on `FLASK_ENV`

### Job Execution (Both Modes)
- API requests (`/api/jobs`, `/api/display`, etc.) trigger background jobs
- ThreadPoolExecutor handles Pixoo updates, font rendering, image generation
- Frontend polls job status until completion

---

## 5. Directory Structure

```
64board/
├── backend/
│   ├── app/
│   │   ├── __init__.py         # Flask factory (create_app)
│   │   ├── models.py           # SQLAlchemy ORM models
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── ui.py           # Template routes
│   │   ├── services/
│   │   │   └── __init__.py
│   │   └── templates/
│   │       ├── base.html       # Base Jinja2 template
│   │       └── index.html      # Main page
│   ├── tests/                  # pytest tests
│   ├── config.py               # Flask configuration
│   ├── wsgi.py                 # WSGI entry point
│   ├── requirements.txt        # Python dependencies
│   └── requirements-dev.txt    # Dev dependencies (pytest, mypy, etc.)
├── frontend/
│   ├── src/                    # TypeScript/SCSS source
│   └── public/                 # Static assets (images, etc.)
├── docs/
│   └── architecture_overview.md
├── AGENTS.md
├── README.md
└── LICENSE
```

**Future additions** (as development progresses):
- `backend/static/dist/` - Vite build output (created by `npm run build`, .gitignore)
- `backend/app/routes/api.py` - JSON API endpoints
- `backend/app/services/pixoo.py` - Pixoo 64 HTTP client
- `backend/app/services/fonts.py` - BMFont renderer
- `backend/app/services/jobs.py` - Background job queue
- `frontend/package.json` - Node dependencies
- `frontend/vite.config.ts` - Vite configuration
- `frontend/tsconfig.json` - TypeScript configuration
- `.gitignore` - Git ignore rules
- `.env.example` - Environment variables template

---

## 6. Document Links
- **SDD:** [`docs/sdd/001_overview.md`](../sdd/001_overview.md)  
- **ADR:** [`docs/adr/0001_choose_db.md`](../adr/0001_choose_db.md)  
- **Root Index:** [`AGENTS.md`](../AGENTS.md)