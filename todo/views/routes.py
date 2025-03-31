from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

# fake
todos = [
    {"id": 1, "title": "complete ", "description": "complete Flask API goal", "completed": False},
]
@api.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

# get all todo
@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# get one todo
@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    return jsonify(todo) if todo else ("", 404)

# create
@api.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "title": data["title"],
        "description": data.get("description", ""),
        "completed": data.get("completed", False),
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# update
@api.route('/todos/<int:id>', methods=['PUT']) 
def update_todo(todo_id):
    data = request.get_json()
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Not found"}), 404
    # update
    for key in data:
        if key in todo:
            todo[key] = data[key]
    return jsonify(todo), 200

# delete
@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return "", 200
