from .exts import db

class Todo(db.Document):
  title = db.StringField(required=True)
  description = db.StringField()
  done = db.BooleanField()
