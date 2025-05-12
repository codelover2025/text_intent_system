from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (you can replace this with database logic later)
sample_data = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Designer"},
    {"id": 3, "name": "Charlie", "role": "Manager"}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API Home!", "status": "ok"})

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(sample_data)

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in sample_data if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'role' not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_user = {
        "id": len(sample_data) + 1,
        "name": data['name'],
        "role": data['role']
    }
    sample_data.append(new_user)
    return jsonify(new_user), 201

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
