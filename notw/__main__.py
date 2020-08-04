from . import ARGS
from . import db_handler as handler

def main():
	""" Executes the main program """
	if argument := ARGS.new:
		handler.add_note(argument)

	if argument := ARGS.delete:
		note_indexes_to_delete = argument

		for index, note_index in enumerate(note_indexes_to_delete):
			handler.delete_note(note_index - index)

	if argument := ARGS.update:
		handler.update_note(argument, ARGS.new_content)

	for item in handler.presentable_data():
		print(item)	

if __name__ == "__main__":
	main()
