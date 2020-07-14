from .tools.database_manager import DatabaseManager
from .tools.note_class import Note, construct_note

# Initialize database
db = DatabaseManager()
db.create_table()

# data modeling
def model_data():
	data = list()
	for item in db.load_all():
		identity, content, unixstamp = item
		item = Note(identity, content, unixstamp)
		data.append(item)
	return data

def presentable_data():
	full_log = list()

	for index, item in enumerate(model_data()):
		new_index, content = str(index + 1), item.content
		fmt = "\t{0}.{2}{1}".format(new_index, content, (" " * 5))
		full_log.append(fmt)
	
	return full_log

# database speakers
get_identity = lambda index : model_data()[index - 1].identity

def add_note(note_content):
	note = construct_note(note_content)
	db.add(note)

def delete_note(index):
	db.delete(get_identity(index))

def update_note(index, new_content):
	db.update(new_content, get_identity(index))

def exit_db():
	db.__del__()
	