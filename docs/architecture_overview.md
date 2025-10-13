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
| Front-End (TypeScript + Tabler UI + SCSS)          |
|  ├─ esbuild (Python subprocess)                    |
|  ├─ libsass / Flask-Assets                         |
|  └─ Static JS / CSS served via Flask               |
+––––––––––––––––––––––––––+

---

## 2. Adopted Technologies

| Layer | Technology | Rationale |
|-------|-------------|------------|
| **Framework** | Flask 3.x | Lightweight, modular, simple to host on Pi |
| **Template Engine** | Jinja2 | Built-in, supports server-side composition |
| **UI Framework** | Tabler UI (Bootstrap 5) | Provides admin components with minimal weight |
| **Language** | TypeScript | Safer client scripting without frameworks |
| **CSS Preprocessor** | SCSS (via libsass) | Style flexibility, Node-free |
| **Bundler** | esbuild (subprocess) | Ultra-fast TS → JS build inside Python |
| **Database** | SQLite + SQLAlchemy 2.x | Zero-config persistence, small footprint |
| **Job Execution** | ThreadPoolExecutor | Simple background jobs; no Celery |
| **Testing** | pytest + coverage | Lightweight and Pi-friendly |

---

## 3. Design Principles

1. **Minimalism:** keep runtime dependencies small and avoid Node.js.  
2. **Transparency:** architecture readable by humans & AI agents alike.  
3. **Separation of concerns:** routes / services / UI clearly divided.  
4. **Extendability:** new renderers or job types can be plugged in without restructuring.

---

## 4. Build and Runtime Flow

1. `flask run` starts the app.  
2. `ensure_dev_builders()` spawns **esbuild** and **libsass** watchers.  
3. TypeScript → JS and SCSS → CSS outputs are written to `/static`.  
4. Flask serves HTML + JS + CSS directly; no extra dev server.  
5. API requests trigger background jobs for Pixoo updates or font generation.  
6. Job status is polled from UI until completion.

---

## 5. Document Links
- **SDD:** [`docs/sdd/001_overview.md`](../sdd/001_overview.md)  
- **ADR:** [`docs/adr/0001_choose_db.md`](../adr/0001_choose_db.md)  
- **Root Index:** [`AGENTS.md`](../AGENTS.md)