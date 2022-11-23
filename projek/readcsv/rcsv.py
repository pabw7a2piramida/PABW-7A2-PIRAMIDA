import csv

rows = []

with open('static/Cars.csv', 'r') as csvfile:
	csvreader = csv.DictReader(csvfile)
	rows = list(csvreader)