"""
Globale Konstanten der Anwendung.
"""

from pathlib import Path

# Projektverzeichnis
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Datenverzeichnis
DATA_DIR = PROJECT_ROOT / "data"

# Standarddatei
DEFAULT_DATASET = DATA_DIR / "spotify_history.csv"

# Unterstützte Dateiformate
SUPPORTED_FILE_TYPES = ["csv"]