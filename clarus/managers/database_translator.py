import time
import collections
from . import database_manager as database

# conversors
def convert_status(status):
	fmt = ["[", " ", "]"]
	fmt[1] = "X" if status else " "
	return "".join(fmt)

# data modeling
def model_data():
	Note = collections.namedtuple("Note", ["identity", "content", "unixstamp", "is_completed"])
	data = []
	for item in database.raw_load:
		item[-1] = convert_status(item[-1])
		item = Note(item[0], item[1], item[2], item[3])
		data.append(item)
	return data

# loads all data
full_log = []
modeled_data = model_data()

for index, item in enumerate(modeled_data):
	status, content = item.is_completed, item.content
	fmt = f"\t{str(index + 1)} {status} {content}"
	full_log.append(fmt)

# database speakers
identity_from_index = lambda index : modeled_data[index -1].identity

def delete_note(note_index):
	database.delete_data(identity_from_index(note_index))

def update_note(note_index, new_content):
	database.update_data(new_content, identity_from_index(note_index))
