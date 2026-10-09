
import csv
import json

# Read data from CSV file
with open("input.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

# Convert data into JSON and save it
with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data converted to JSON successfully!")
