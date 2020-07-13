import json

from flask import Flask
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# placeholder to keep data
db = dict()

# Create the API
api = Api(app)


class AddBooks(Resource):
    def post(self):
        with open('./data/books.json') as f:
            books = json.load(f)
        db['book'] = books
        return {'message': 'Books added'}, 201


class FriendList(Resource):
    def get(self):
        friends_list = [db]

        friends = []

        for key in friends_list:
            friends.append(key)
        return {'message': 'Success', 'data': friends}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('phone', required=True)

        # Parse the argument into object
        args = parser.parse_args()

        db[args['identifier']] = args

        return {'message': 'Feiend registered', 'data': args}, 201


class Friend(Resource):
    def get(self, identifier):
        friend = db

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in friend):
            return {'message': 'Friend not found', 'data': {}}, 404

        return {'message': 'Friend found', 'data': friend[identifier]}, 200

    def delete(self, identifier):
        friend = db

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in friend):
            return {'message': 'Friend not found', 'data': {}}, 404

        del friend[identifier]
        return '', 204


api.add_resource(FriendList, '/friends')
api.add_resource(Friend, '/friend/<string:identifier>')
api.add_resource(AddBooks, '/book')
