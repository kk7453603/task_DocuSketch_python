from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://db:27017')
db = client.mydatabase


@app.route('/api/keyvalue', methods=['POST'])
def create_key_value():
    key = request.json['key']
    value = request.json['value']
    db.mycollection.insert_one({'key': key, 'value': value})
    return jsonify({'message': 'Value created'})


@app.route('/api/keyvalue/<string:key>', methods=['PUT'])
def update_key_value(key):
    new_value = request.json['value']
    db.mycollection.update_one({'key': key}, {'$set': {'value': new_value}})
    return jsonify({'message': 'Value updated'})


@app.route('/api/keyvalue/<string:key>', methods=['GET'])
def get_key_value(key):
    result = db.mycollection.find_one({'key': key})
    if result:
        return jsonify({'value': result['value']})
    else:
        return jsonify({'message': 'Value not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
