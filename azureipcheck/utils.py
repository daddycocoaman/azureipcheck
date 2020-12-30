from pathlib import Path
from typing import List

from . import app_dir


def get_service_json_files() -> List[Path]:
    return Path(app_dir).glob("ServiceTags_*.json")