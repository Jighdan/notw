import os
import sqlite3
from .tools.note_class import construct_note

# database paths and name
db_filename, db_name = "notes.db", "allNotes"
db_path = os.path.join(os.getcwd(), db_filename)
# initializes the database and cursor for raw loading
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
# database fields
fields = "identity TEXT, content TEXT, unixstamp TIMESTAMP, is_completed BOOLEAN"
# common sql queries
select_all = f"SELECT * FROM {db_name}"
# creates the database if doesn't exists
cursor.execute(f"CREATE TABLE IF NOT EXISTS {db_name}({fields})")

# back-end controllers
def raw_load_all():
	cursor = connection.cursor()
	cursor.execute(select_all)
	raw_load = [list(item) for item in cursor.fetchall()]
	cursor.close()
	return raw_load

raw_load = raw_load_all()

# user interfance controllers
def add_data(note_content):
	note = construct_note(note_content)
	identity, content = note.identity, note.content
	unixstamp, is_completed = note.unixstamp, note.is_completed
	cursor.execute(f"INSERT INTO {db_name} VALUES (?, ?, ?, ?)", (identity, content, unixstamp, is_completed))
	connection.commit()

def delete_data(data_identity):
	cursor = connection.cursor()
	cursor.execute(select_all)
	cursor.execute(f"DELETE FROM {db_name} WHERE identity = '{data_identity}'")
	cursor.close()
	connection.commit()

def update_data(new_content, data_identity):
	cursor = connection.cursor()
	cursor.execute(select_all)
	cursor.execute(f"UPDATE {db_name} SET content = '{new_content}' WHERE identity = '{data_identity}'")
	cursor.close()
	connection.commit()
