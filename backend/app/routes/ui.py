from flask import Blueprint, render_template

ui_bp = Blueprint("ui", __name__)


@ui_bp.get("/")
def dashboard():
    return render_template("dashboard.html", page_name="dashboard", page_context="")


@ui_bp.get("/scenes/")
def scenes():
    return render_template("scenes.html", page_name="scenes", page_context="")


@ui_bp.get("/apps/")
def apps():
    return render_template("apps/index.html", page_name="apps", page_context="")


@ui_bp.get("/channels/")
def channels():
    return render_template("channels.html", page_name="channels", page_context="")
