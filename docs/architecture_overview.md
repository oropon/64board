# Architecture Overview — 64board

## 1. High-Level Architecture
+––––––––––––––––––––––––––+
| Flask (Python 3.12)                                |
|  ├─ routes/ui.py        → HTML templates (Jinja2)  |
|  ├─ routes/api.py       → REST JSON endpoints      |
|  ├─ services/pixoo.py   → Pixoo 64 HTTP API        |
|  ├─ services/fonts.py   → BMFont rendering (bmfontify) |
|  ├─ services/jobs.py    → Job queue (ThreadPoolExecutor) |
|  └─ models.py           → SQLite ORM models        |
+––––––––––––––––––––––––––+
│
│ JSON / REST
▼
+––––––––––––––––––––––––––+
| Front-End (Node + Vite + TypeScript + SCSS)        |
|  ├─ Vite dev server (proxy to Flask in dev)       |
|  ├─ TypeScript + Tabler UI + SCSS                 |
|  └─ Built assets served via Flask in production   |
+––––––––––––––––––––––––––+

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
1. `npm run dev` (or `vite`) starts Vite dev server with HMR.
2. Vite proxies API requests to Flask backend (`flask run` on separate port).
3. TypeScript and SCSS are compiled on-the-fly by Vite.
4. Frontend served by Vite (typically `localhost:5173`), backend on `localhost:5000`.

### Production Mode
1. `npm run build` (or `vite build`) bundles TypeScript + SCSS → `/static/dist`.
2. `flask run` serves HTML templates and static assets directly.
3. No separate frontend server; Flask handles all routes.

### Job Execution (Both Modes)
5. API requests trigger background jobs for Pixoo updates or font generation.
6. Job status is polled from UI until completion.

---

## 5. Document Links
- **SDD:** [`docs/sdd/001_overview.md`](../sdd/001_overview.md)  
- **ADR:** [`docs/adr/0001_choose_db.md`](../adr/0001_choose_db.md)  
- **Root Index:** [`AGENTS.md`](../AGENTS.md)