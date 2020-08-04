from collections import namedtuple
from datetime import datetime
import uuid

# generators
generate_identity = lambda : str(uuid.uuid4())
generate_unixstamp = lambda : datetime.utcnow()

Note = namedtuple("Note", ["identity", "content", "unixstamp"])

def construct_note(content):
	""" Structures note to (named) tuple """
	identity = generate_identity()
	unixstamp = generate_unixstamp()
	structured = Note(identity, content, unixstamp)
	return structured
	