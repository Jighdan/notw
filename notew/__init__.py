# sets parser and adds arguments
parser = argparse.ArgumentParser(description="Notes & Tasker App")
parser.add_argument("-n", "--new", type=str, dest="new_note", help="Adds a new note")
parser.add_argument("-d", "--delete", type=int, dest="delete_note", help="Deletes a note")
parser.add_argument("-u", "--update", type=int, dest="update_note", help="Updates a note content")
parser.add_argument("-c", "--content", type=str, dest="new_content", required="--update" in sys.argv)

args = parser.parse_args()