from datetime import datetime
import uuid

class Note:
	def __init__(self, content):
		self.content = content
		self.timestamp = self.__set_timestamp()
		self.is_completed = False
		self.identity = self.__set_identity()

	def __set_timestamp(self):
		today = datetime.now()
		formated_date = today.strftime("%-I:%M %p / %a %d %b %Y")
		return formated_date

	def __set_identity(self):
		generate_identity = uuid.uuid4()
		return generate_identity

	def __repr__(self):
		note = dict()
		note["content"] = self.content
		note["timestamp"] = self.timestamp
		note["is_completed"] = self.is_completed
		note["identity"] = self.identity
		return note
