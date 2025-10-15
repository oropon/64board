from flask import Blueprint, render_template

ui_bp = Blueprint("ui", __name__)


@ui_bp.get("/")
def index():
    return render_template("index.html", message="Hello, Tabler!")
