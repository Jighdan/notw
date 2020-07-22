import os
from pathlib import Path

db_dir = str(Path.home())
db_file = "notes.db"
db_table = "allNotes"

db_path = os.path.join(db_dir, db_file)
