import os
from pathlib import Path

DB_DIR = str(Path.home())
DB_FILE = "notes.db"

DB_TABLENAME = "allNotes"
DB_PATHDIR = os.path.join(DB_DIR, DB_FILE)
