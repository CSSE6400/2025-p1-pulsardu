from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

# 假数据
todos = [
    {"id": 1, "title": "complete", "description": "complete Flask API goal", "completed": False},
]

# 健康检查
@api.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

# 获取所有 TODO
@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# 获取单个 TODO
@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    return (jsonify(todo), 200) if todo else ("", 404)

# 创建 TODO
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

# ✅ 修复：更新 TODO（添加了装饰器）
@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    todo = next((item for item in todos if item['id'] == id), None)
    if not todo:
        return jsonify({"error": "Not found"}), 404
    # 更新字段
    for key in ['title', 'description', 'completed']:
        if key in data:
            todo[key] = data[key]
    return jsonify(todo), 200

# 删除 TODO
@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return "", 200
