from flask import Blueprint, request, Response, url_for

# from ..models import Todo
from ..pymongo import Todo

api = Blueprint('todo', __name__)

# query todolist
@api.route('/todos/', methods=['GET'])
def get_todos():
  # todos = Todo.objects().to_json()
  todos = Todo.to_json(Todo.queryTodoList())

  return Response(todos, mimetype='application/json', status=200)


# create a todo
@api.route('/todos/', methods=['POST'])
def create_todo():
  body = request.get_json()

  # todo = Todo(**body).save()
  inserted_id = str(Todo.addTodo(body))

  return { 'id': inserted_id, 'success': True }, 200


# query single todo
@api.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
  # todo = Todo.objects(id=todo_id).to_json()
  todo = Todo.to_json(Todo.queryTodoById(todo_id))

  return Response(todo, mimetype='application/json', status=200)


# update 
@api.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
  todo = request.get_json()

  # Todo.objects(id=todo_id).update(**todo)
  Todo.updateTodo(todo_id, todo)

  return { 'success': True }, 200


# delete
@api.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
  # Todo.objects(id=todo_id).delete()
  Todo.deleteTodo(todo_id)

  return { 'success': True }, 200
