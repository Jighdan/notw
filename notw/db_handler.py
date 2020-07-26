from .tools.db_manager import DatabaseManager
from .tools.note_constructor import Note, construct_note

# Initialize database
db = DatabaseManager()

# Data modeling
def model_data():
	""" Structures the data in the database """
	data = list()
	for item in db.load_all():
		identity, content, unixstamp = item
		item = Note(identity, content, unixstamp)
		data.append(item)
	return data

def presentable_data():
	""" Formats data to a presentable state """
	full_log = list()

	for index, item in enumerate(model_data()):
		new_index, content = str(index + 1), item.content
		fmt = "\t{0}.{2}{1}".format(new_index, content, (" " * 5))
		full_log.append(fmt)
	
	return full_log

# Database handlers
get_identity = lambda index : model_data()[index - 1].identity

def add_note(note_content):
	""" Handles adding notes to the database """
	note = construct_note(note_content)
	db.add(note)

def delete_note(index):
	""" Handles deleting notes in the database """
	db.delete(get_identity(index))

def update_note(index, new_content):
	""" Handles updating notes in the database """
	db.update(new_content, get_identity(index))
	