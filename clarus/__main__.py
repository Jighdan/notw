import argparse
from blessings import Terminal
from modules.note_class import Note
from modules import database_manager

# initializes terminal
term = Terminal()

# sets parser and adds arguments
PARSER = argparse.ArgumentParser(description="Notes & Tasker App")
PARSER.add_argument("-n", "--new", dest="new_note", help="Adds a new note")
args = PARSER.parse_args()

def present_tasks():
	data = database_manager.raw_load_all()
	for index, item in enumerate(data):
		content = item["content"]
		timestamp = item["timestamp"]
		is_completed = "~" if item["is_completed"] else " "

		print(f"{str(index)}. {term.bold(content)}")


if __name__ == '__main__':
	if args.new_note:
		database_manager.save(Note(args.new_note))

	present_tasks()