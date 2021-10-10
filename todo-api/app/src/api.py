from flask import Flask, jsonify
from flask_restx import Resource, Api
from models.todo_model import Todo

app = Flask(__name__)

api = Api(app)

# Instantiate object form Todo class to store tasks
TODOS = Todo()


@api.route('/api/v1/todo')
class Tasks(Resource):
    def get(self):
        return TODOS.get_tasks()


@api.route('/api/v1/todo/add/<string:content>')
class Create(Resource):
    def post(self, content):
        task_id = TODOS.create_task(content=content)
        return jsonify({
            'task_id': task_id,
            'status': 200
        })


@api.route('/api/v1/todo/update_content/<string:task_id>/<string:content>')
class UpdateContent(Resource):
    def put(self, task_id, content):
        response_status, response_message = TODOS.update_task_content(
            task_id=task_id, content=content)
        return jsonify({
            'status': response_status,
            'message': response_message
        })


@api.route('/api/v1/todo/update_status/<string:task_id>/<string:status>')
class UpdateStatus(Resource):
    def put(self, task_id, status):
        response_status, response_message = TODOS.update_task_status(
            task_id=task_id, status=status)
        return jsonify({
            'status': response_status,
            'message': response_message
        })


@api.route('/api/v1/todo/delete/<string:task_id>')
class Delete(Resource):
    def delete(self, task_id):
        response_status, response_message = TODOS.delete_task(task_id)
        return jsonify({
            'status': response_status,
            'message': response_message
        })


if __name__ == '__main__':
    app.run(debug=True, port="80", host="0.0.0.0")
