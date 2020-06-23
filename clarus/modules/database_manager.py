import os
import csv

db_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
db_filename = "notes.csv"
db_path = os.path.join(db_dir, db_filename)

fields = ["content", "timestamp", "is_completed", "identity"]

def raw_load_all():
	with open(db_path, "r") as csv_file:
		reader = csv.DictReader(csv_file)
		items = (dict(item) for item in reader)
		return [item for item in items] if True else False
	
def save(note):
	with open(db_path, "a") as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fields)
		writer.writerow(note.copy())
