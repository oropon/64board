import json
from pathlib import Path
from typing import List, Union
from flask import Flask


def init_vite_manifest(app: Flask) -> None:
    manifest_path = Path(app.config["VITE_MANIFEST_PATH"])
    with manifest_path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)

    def vite_asset(entry: str, asset_type: str = "file") -> Union[str, List[str]]:
        entry_data = manifest[entry][asset_type]
        if asset_type == "css":
            return _prefix_list(entry_data)
        if isinstance(entry_data, list):
            return _prefix_list(entry_data)
        return _prefix_path(entry_data)

    app.jinja_env.globals["vite_asset"] = vite_asset


def _prefix_path(asset_path: str) -> str:
    return f"dist/{asset_path}"


def _prefix_list(paths: List[str]) -> List[str]:
    return [_prefix_path(path) for path in paths]
