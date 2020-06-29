from collections import namedtuple
from datetime import datetime
import uuid

# generators
generate_identity = lambda : str(uuid.uuid4())
generate_unixstamp = lambda : datetime.utcnow()

# note deconstructor
Note = namedtuple("Note", ["identity", "content", "unixstamp"])

def construct_note(note_content):
	identity = generate_identity()
	content = note_content
	unixstamp = generate_unixstamp()
	structured = Note(identity, content, unixstamp)
	return structured
	