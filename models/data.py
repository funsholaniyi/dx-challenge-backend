import csv
import json


class ProductionModel:

    def __init__(self):
        with open('./data/cleaned_data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            out = json.dumps([row for row in csv_reader])

        # Save the JSON
        f = open('./parsed.json', 'w')
        f.write(out)
