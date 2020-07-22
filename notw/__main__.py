import argparse
import sys
from . import db_handler as handler

# sets parser and adds arguments
parser = argparse.ArgumentParser(description="Notes & Tasker App")
parser.add_argument("-n", "--new", type=str, help="Adds a new note")
parser.add_argument("-d", "--delete", type=int, nargs='*', help="Deletes a note")
parser.add_argument("-u", "--update", type=int, help="Updates a note's content")
parser.add_argument("-c", "--new_content", type=str, required="--update" in sys.argv)

args = parser.parse_args()

def main():
	if argument := args.new:
		handler.add_note(argument)

	if argument := args.delete:
		note_indexes_to_delete = argument

		# for each note index, subtract the number of notes that have already been deleted,
		# this accounts for the number of notes becoming smaller with each cycle
		for i, note_index in enumerate(note_indexes_to_delete):
			handler.delete_note(note_index - i)

	if argument := args.update:
		handler.update_note(argument, args.new_content)

	for item in handler.presentable_data():
		print(item)	

	handler.exit_db()

if __name__ == "__main__":
	main()
