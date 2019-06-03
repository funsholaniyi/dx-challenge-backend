from flask import Flask
from flask_restful import Resource, Api

from models.data import ProductionModel

app = Flask(__name__)
api = Api(app)
model = ProductionModel()


class DataEntryGate(Resource):
    def get(self):
        return model.get_data()


api.add_resource(DataEntryGate, '/')

if __name__ == '__main__':
    app.run(debug=True)
