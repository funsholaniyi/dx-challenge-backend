import csv
import json


class ProductionModel:

    def __init__(self):
        with open('./data/cleaned_data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            out = json.dumps([row for row in csv_reader])
        # Save the JSON
        f = open('./parsed_data.json', 'w')
        f.write(out)


    def get_data(self):
        json_data = open('parsed_data.json')
        data = json.load(json_data)
        return data
