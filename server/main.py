from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

SHOPPINGLIST = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'}
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in SHOPPINGLIST:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return SHOPPINGLIST[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del SHOPPINGLIST[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all SHOPPINGLIST, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return SHOPPINGLIST

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(SHOPPINGLIST.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        SHOPPINGLIST[todo_id] = {'task': args['task']}
        return SHOPPINGLIST[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)