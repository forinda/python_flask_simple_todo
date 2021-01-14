from todo import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), index=True)
    time = db.Column(db.DateTime,index=True, default=datetime.now())
    done = db.Column(db.Boolean, default=False)
    updated = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"<Todo: {self.body}>"

    h = datetime.now().strftime("")