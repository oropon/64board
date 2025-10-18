from flask import Blueprint, render_template

ui_bp = Blueprint("ui", __name__)


@ui_bp.get("/")
def dashboard():
    return render_template("dashboard.html", page_name="dashboard", page_context="")
