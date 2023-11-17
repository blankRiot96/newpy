import os
from pathlib import Path

USER_PATH = Path(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")).parent

SAVE_FILE = Path(USER_PATH / "assets" / "temp_dir.txt")
if not SAVE_FILE.exists():
    SAVE_FILE.touch()

with open(SAVE_FILE) as f:
    content = f.read()


TEMPLATE_PATH = Path(content) if content else None
