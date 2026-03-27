from pathlib import Path

UNIT_DIR = Path(__file__).parent
DATA_DIR = UNIT_DIR / "data"
notes_path = DATA_DIR / "notes.txt"
print(UNIT_DIR)