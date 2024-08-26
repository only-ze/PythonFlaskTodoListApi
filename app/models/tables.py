from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable =False)
    complete = db.Column(db.Boolean, default = False)

    def to_dict(self):
        return{
            'id' : self.id,
            'task' : self.task,
            'complete': self.complete
        }