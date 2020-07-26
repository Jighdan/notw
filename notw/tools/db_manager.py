import sqlite3
from .. import db_path, db_table

class DatabaseManager:
	def __init__(self):
		""" Loads database """
		self.connection = sqlite3.connect(db_path)
		self.sql_fields = "identity TEXT, content TEXT, unixstamp TIMESTAMP"

		# Generates a table if it doesn't exists
		table_query = f"CREATE TABLE IF NOT EXISTS {db_table}({self.sql_fields})"
		self._execute(table_query)

	def __del__(self):
		""" Closes the database """
		self.connection.close()

	def _execute(self, statement):
		""" Executes a SQL query in the database """
		with self.connection:
			cursor = self.connection.cursor()
			cursor.execute(statement)
			return cursor

	def load_all(self):
		""" Loads all the items from the database """
		query = f"SELECT * FROM {db_table}"
		raw_data = self._execute(query)
		return [list(item) for item in raw_data.fetchall()]

	# CRUD statements
	def add(self, data):
		""" Adds data to the database """
		query = f"""
			INSERT INTO {db_table} 
			VALUES ('{data.identity}', '{data.content}', '{data.unixstamp}')
		"""
		self._execute(query)
		self.connection.commit()

	def delete(self, data_identity):
		""" Deletes data from the database """
		query = f"DELETE FROM {db_table} WHERE identity = '{data_identity}'"
		self._execute(query)
		self.connection.commit()

	def update(self, new_content, data_identity):
		""" Updates data from the database """
		query = f"UPDATE {db_table} SET content = '{new_content}' WHERE IDENTITY = '{data_identity}'"
		self._execute(query)
		self.connection.commit()
