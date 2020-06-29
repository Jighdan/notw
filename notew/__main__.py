import argparse
import sys
from . import args
from .database_manager as database
from .database_translator as translator

def main():
	for item in translator.full_log:
		print(item)

	if argument := args.new_note:
		database.add_data(argument)

	if argument := args.delete_note:
		translator.delete_note(argument)
	
	if argument := args.update_note:
		translator.update_note(argument, args.new_content)

if __name__ == "__main__":
	main()