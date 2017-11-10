# flask-rest API
A quick howto to setup a flask api that reads from a json file and appends posts.
This isn't efficient code nor is it error proof. It's mainly a quick setup for testing purposes.

## Requirements
Create a venv
```
virtualenv apiVenv
source apiVenv/bin/activate
```
Install Flask & Flast-restful
```
pip install flask
pip install flask-restful
```
Add your data in data.json, and run the api.
```
python flask-api.py
```

## Testing the code
Get all:
curl http://127.0.0.1:5000/list

Get at index:
curl http://127.0.0.1:5000/list/0

Post:
curl http://127.0.0.1:5000/list -d '{"name":"newName","label":"newLabel"}' -X POST -H "Content-Type: application/json"

## Different data
When using different data, be sure to update the parser in flask-api.py.
```
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('label')
```
