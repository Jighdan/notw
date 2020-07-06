import time
from .tools.note_class import Note, construct_note
from . import database_manager as database

# data modeling
def model_data():
	data = []
	for item in database.raw_load_all():
		identity, content, unixstamp = item
		item = Note(identity, content, unixstamp)
		data.append(item)
	return data

def presentable_data():
	modeled_data, full_log = model_data(), list()
	for index, item in enumerate(modeled_data):
		new_index, content = str(index + 1), item.content
		fmt = "\t{0}.{2}{1}".format(new_index, content, (" " * 5))
		full_log.append(fmt)
	
	return full_log

# database speakers
get_identity = lambda index : modeled_data[index - 1].identity

def add_note(note_content):
	note = construct_note(note_content)
	database.add_data(note)

def delete_note(note_index):
	database.delete_data(get_identity(note_index))

def update_note(note_index, new_content):
	database.update_data(new_content, get_identity(note_index))

def exit_database():
	database.connection.close()