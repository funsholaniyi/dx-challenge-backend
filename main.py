from flask import Flask
from flask_restful import Resource, Api

from models.data import ProductionModel

app = Flask(__name__)
api = Api(app)


class DataEntryGate(Resource):
    def get(self):
        ProductionModel()
        return {'hello': 'world'}


api.add_resource(DataEntryGate, '/')

if __name__ == '__main__':
    app.run(debug=True)
