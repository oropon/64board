from flask import Flask
from pathlib import Path
from flask.helpers import get_debug_flag
from dotenv import load_dotenv
from .vite import init_vite_manifest


def create_app() -> Flask:
    base_dir = Path(__file__).resolve().parent.parent
    static_folder = base_dir / "static"

    app = Flask(__name__, static_folder=str(static_folder))

    load_dotenv(base_dir / ".env")
    app.config["DEBUG"] = get_debug_flag()
    app.config.setdefault("USE_VITE_DEV_SERVER", app.debug)
    app.config.setdefault(
        "VITE_MANIFEST_PATH", static_folder / "dist" / "manifest.json"
    )

    if not app.config["USE_VITE_DEV_SERVER"]:
        init_vite_manifest(app)

    from .routes.ui import ui_bp

    app.register_blueprint(ui_bp)

    return app
