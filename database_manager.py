import csv
import pandas as pd

database_name = "notes.csv"
fields = ["content", "timestamp", "is_completed", "identity"]

def raw_load_all():
	with open(database_name, "r") as csv_file:
		reader = csv.DictReader(csv_file)
		return [dict(item) for item in reader]

def present_database():
	data = raw_load_all()
	if len(data) > 0:
		for item in data:
			print("{} | {}".format(item["content"], item["timestamp"]))
	else:
		print("No Data")
	
def save(note):
	with open(database_name, "a") as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fields)
		writer.writerow(note.copy())

# Initialize Database
dataframe = pd.read_csv(database_name)
if dataframe.empty:
	with open(database_name, "w") as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fields)
		writer.writeheader()