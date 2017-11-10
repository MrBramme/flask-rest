from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)
with open('data.json') as data_file:    
    jsonData = json.load(data_file)
notFound = {
        "message": "A resource with that ID no longer exists.",
        "status": 410};

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('label')

class List(Resource):
    def get(self):
        return jsonData;
    
    def post(self):
        args = parser.parse_args()
        print(args)
        with open('data.json', 'w') as outfile:
            jsonData.append(args)
            json.dump(jsonData, outfile)
        return jsonData, 200

class Get_Item(Resource):
    def get(self,itemNr):
        if itemNr >= len(jsonData):
            return notFound;
        return jsonData[0];

api.add_resource(Get_Item, '/list/<int:itemNr>')
api.add_resource(List, '/list')

if __name__ == '__main__':
     app.run(host='0.0.0.0')
