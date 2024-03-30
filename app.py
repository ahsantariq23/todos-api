import json
import pdb

from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)
todos = {
    1: {"task": "Complete project proposal", "summary": "Finish writing and formatting the project proposal document"},
    2: {"task": "Buy groceries", "summary": "Purchase items for the week's meals"},
    3: {"task": "Call the plumber", "summary": "Schedule a visit to fix the leaky faucet in the bathroom"}
}


class ToDo(Resource):
    def get(self):
        print(json.dumps(todos, indent=4))
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True, location='args')
        args = parser.parse_args(req=request)
        id = args["id"]
        if id not in todos:
            return {"error": "Task with specified id not found"}, 400
        return {"data": todos[id]}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("task", type=str, help="Task is required", required=True, location='json')
        parser.add_argument("summary", type=str, help="Summary is Required", required=True, location='json')
        args = parser.parse_args()
        id = len(todos) + 1
        todos[id] = {"task": args["task"], "summary": args["summary"]}
        return {"data": todos[id]}, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("task", type=str, help="Task is required", location='json')
        parser.add_argument("summary", type=str, help="Summary is Required", location='json')
        parser.add_argument("id", type=int, help="id is Required", required=True, location='json')
        args = parser.parse_args()
        id = args.get("id")
        if id not in todos:
            abort(409, "Cant update id does not exists")
        if args['task']:
            todos[id]['task'] = args['task']
        if args['summary']:
            todos[id]['summary'] = args['summary']
        return {"msg": f"Successfully updated task with id={id}", "data": todos}, 200


api.add_resource(ToDo, '/todo')

if __name__ == '__main__':
    app.run(host='localhost', port=8088, debug=True)
