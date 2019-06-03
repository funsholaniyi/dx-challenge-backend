from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

from models.data import ProductionModel

app = Flask(__name__)
CORS(app)

api = Api(app)
model = ProductionModel()


class DataEntryGate(Resource):
    def get(self):
        return model.get_data()


api.add_resource(DataEntryGate, '/')

if __name__ == '__main__':
    app.run(debug=True)
