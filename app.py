from flask import Flask
from flask_restful import Resource, Api,reqparse,abort
app=Flask(__name__)
api=Api(app)
todos = {
   1: {"task": "Complete project proposal", "summary": "Finish writing and formatting the project proposal document"},
   2: {"task": "Buy groceries", "summary": "Purchase items for the week's meals"},
   3: {"task": "Call the plumber", "summary": "Schedule a visit to fix the leaky faucet in the bathroom"}
   
}

parser=reqparse.RequestParser()
parser.add_argument("task", type=str ,help="Task is required", required=True)
parser.add_argument("summary", type=str, help="Summary is Required", required=True)


class todoList(Resource):
    def get(self):
        return todos
    
    

class todo(Resource):
    def get(self,id):
        if id >= len(todos):
            return "out of range"
        return todos[id]
    
    def post(self,id):
        args=parser.parse_args()
        if id in todos:
            abort(409,"Task already exists")
        todos[id]={"task" : args["task"], "summary":args["summary"]}
        return todos[id]




api.add_resource(todoList,'/todos')
api.add_resource(todo,'/todo/<int:id>')

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088,debug=True)
