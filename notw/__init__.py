import os
from pathlib import Path

# Directory of the database
db_dir = str(Path.home())
# Filename of the database
db_file = "notes.db"
# Name of the table containing the notes
db_table = "allNotes"

# Full path of the database
db_path = os.path.join(db_dir, db_file)
