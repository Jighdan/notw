import argparse
import sys
from . import database_translator as translator

# sets parser and adds arguments
parser = argparse.ArgumentParser(description="Notes & Tasker App")
parser.add_argument("-n", "--new", type=str, help="Adds a new note")
parser.add_argument("-d", "--delete", type=int, help="Deletes a note")
parser.add_argument("-u", "--update", type=int, help="Updates a note content")
parser.add_argument("-c", "--new_content", type=str, required="--update" in sys.argv)

args = parser.parse_args()

def main():
	if argument := args.new:
		translator.add_note(argument)

	if argument := args.delete:
		translator.delete_note(argument)
	
	if argument := args.update:
		translator.update_note(argument, args.new_content)

	for item in translator.presentable_data():
		print(item)	

	translator.exit_db()

if __name__ == "__main__":
	main()
