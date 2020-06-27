from datetime import datetime
import uuid

class Note:
	def __init__(self, content):
		self.identity = self.__set_identity()
		self.content = content
		self.unixstamp = datetime.utcnow()
		self.is_completed = False

	def __repr__(self):
		return self.content

	def pack(self):
		note = dict()
		note["identity"] = self.identity
		note["content"] = self.content
		note["unixstamp"] = self.unixstamp
		note["is_completed"] = self.is_completed
		return note

	def __set_identity(self):
		generate_identity = uuid.uuid4()
		return str(generate_identity)
