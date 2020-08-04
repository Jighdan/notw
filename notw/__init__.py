import argparse
import sys

parser = argparse.ArgumentParser(description="Notes & Tasker App")
parser.add_argument("-n", "--new", type=str, help="Adds a new note")
parser.add_argument("-r", "--remove", type=int, nargs='*', help="Removes a note")
parser.add_argument("-u", "--update", type=int, help="Updates a note's content")
parser.add_argument("-c", "--new_content", type=str, required="--update" in sys.argv)

ARGS = parser.parse_args()
