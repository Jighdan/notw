import os
import sqlite3
from . import db_path, db_table

# initializes the database and cursor for raw loading
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
# database fields
sql_fields = "identity TEXT, content TEXT, unixstamp TIMESTAMP"
# common sql queries
select_all = "SELECT * FROM {0}".format(db_table)
# creates the database if doesn't exists
cursor.execute("CREATE TABLE IF NOT EXISTS {0}({1})".format(db_table, sql_fields))

# back-end controllers
def raw_load_all():
	cursor = connection.cursor()
	cursor.execute(select_all)
	raw_load = [list(item) for item in cursor.fetchall()]
	cursor.close()
	return raw_load

# user interfance controllers
def add_data(note):
	identity, content, unixstamp = note.identity, note.content, note.unixstamp
	cursor.execute("INSERT INTO {0} VALUES (?, ?, ?)".format(db_table), (identity, content, unixstamp))
	connection.commit()

def delete_data(data_identity):
	cursor = connection.cursor()
	cursor.execute(select_all)
	cursor.execute("DELETE FROM {0} WHERE identity = '{1}'".format(db_table, data_identity))
	cursor.close()
	connection.commit()

def update_data(new_content, data_identity):
	cursor = connection.cursor()
	cursor.execute(select_all)
	cursor.execute(f"UPDATE {0} SET content = '{1}' WHERE identity = '{2}'".format(db_table, new_content, data_identity))
	cursor.close()
	connection.commit()
	