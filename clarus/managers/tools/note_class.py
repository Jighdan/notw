from collections import namedtuple
from datetime import datetime
import uuid

# generators
generate_identity = lambda : str(uuid.uuid4())
generate_unixstamp = lambda : datetime.utcnow()

# note deconstructor
Note = collections.namedtuple("Note", ["identity", "content", "unixstamp", "is_completed"])

def construct_note(note_content):
	identity = generate_identity()
	content = note_content
	unixstamp = generate_unixstamp()
	is_completed = False
	structured = Note(identity, content, unixstamp, is_completed)
	return structured
	