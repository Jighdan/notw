import sqlite3
from . import DB_TABLENAME, DB_PATHDIR

class DatabaseManager:
	def __init__(self):
		""" Loads database """
		self.connection = sqlite3.connect(DB_PATHDIR)
		self.sql_fields = "identity TEXT, content TEXT, unixstamp TIMESTAMP"

		# Generates a table if it doesn't exists
		table_query = f"CREATE TABLE IF NOT EXISTS {DB_TABLENAME}({self.sql_fields})"
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
		query = f"SELECT * FROM {DB_TABLENAME}"
		raw_data = self._execute(query)
		return [list(item) for item in raw_data.fetchall()]

	# CRUD statements
	def add(self, data):
		""" Adds data to the database """
		query = f"""
			INSERT INTO {DB_TABLENAME} 
			VALUES ('{data.identity}', '{data.content}', '{data.unixstamp}')
		"""
		self._execute(query)
		self.connection.commit()

	def delete(self, data_identity):
		""" Deletes data from the database """
		query = f"DELETE FROM {DB_TABLENAME} WHERE identity = '{data_identity}'"
		self._execute(query)
		self.connection.commit()

	def update(self, new_content, data_identity):
		""" Updates data from the database """
		query = f"UPDATE {DB_TABLENAME} SET content = '{new_content}' WHERE IDENTITY = '{data_identity}'"
		self._execute(query)
		self.connection.commit()
