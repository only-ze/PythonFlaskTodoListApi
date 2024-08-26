from app import app, render_template, request, jsonify, todos, db
from app.models import Todo

@app.route('/api')
def index():
    return "welcome to the api"

@app.route('/api/task', methods=['GET'])
def get_task():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos]), 200

@app.route('/api/task', methods=['POST'])
def add_task():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'task data is required'}), 400
    
    new_task = Todo(task=data)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201


@app.route('/api/task/<int:id>', methods = ['PUT'])
def update_task(id):
    todo = Todo.query.get(id)
    if not todo:
        return jsonify({'error': 'Task Not Found'}), 404
    data = request.json
    todo.task= data.get('task', todo.task)
    todo.complete = data.get('complete') == 'true'
    db.session.commit()
    return jsonify(todo.to_dict()), 200

@app.route('/api/task/<int:id>', methods =['DELETE'])
def delete_task(id):
    todo = Todo.query.get(id)
    if not todo:
        return jsonify({'error': 'Task not found'}), 404
    
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'Warning':'Task deleted'}), 200