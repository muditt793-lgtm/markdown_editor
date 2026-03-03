# Markdown Editor Configuration

import os
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"

DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Application settings
APP_NAME = "Markdown Editor"
APP_VERSION = "2.0.0"
DEBUG = True

# UI Settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"

# Editor settings
AUTO_SAVE = True
AUTO_SAVE_INTERVAL = 30000  # 30 seconds
SYNTAX_HIGHLIGHTING = True
LINE_NUMBERS = True

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = LOGS_DIR / f"editor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Colors
COLORS = {
    "editor_bg": "#252526",
    "editor_text": "#d4d4d4",
    "preview_bg": "#f5f5f5",
    "preview_text": "#333333",
    "header_bg": "#333333",
    "button_bg": "#0078d4",
    "button_hover": "#1084d7"
}

# Fonts
FONTS = {
    "editor": ("Consolas", 11),
    "preview": ("Segoe UI", 10),
    "code": ("Courier New", 9)
}

if __name__ == "__main__":
    print(f"Configuration loaded for {APP_NAME}")
