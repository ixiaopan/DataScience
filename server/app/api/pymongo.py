from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps, loads

class TodoDB():
  def __init__(self):
    client = MongoClient('mongodb://localhost')

    db = client.demo

    self.db = db

    self.collection = db.todo
  

  def to_json(self, str):
    return dumps(str)


  def from_json(self, json):
    return loads(json)


  def queryTodoList(self):
    cursor = self.collection.find()
    
    todoList = [ todo for todo in cursor ]

    return todoList


  def addTodo(self, todo):
    new_todo = self.collection.insert_one(todo)

    return new_todo.inserted_id


  def queryTodoById(self, id):
    todo = self.collection.find_one({ '_id': ObjectId(id) })

    return todo


  def updateTodo(self, id, partital):
    condition = {
      '_id': ObjectId(id)
    }

    self.collection.update_one(condition,{ '$set': partital })

    return True


  def deleteTodo(self, todo_id):
    self.collection.delete_one({ '_id': ObjectId(todo_id) })

    return True

Todo = TodoDB()
