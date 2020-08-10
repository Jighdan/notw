from collections import namedtuple
from datetime import datetime
import uuid

Note = namedtuple("Note", ["identity", "content", "unixstamp"])

def construct_note(content):
	""" Structures note to (named) tuple """
	identity = str(uuid.uuid4())
	unixstamp = datetime.utcnow()
	structured = Note(identity, content, unixstamp)
	return structured
