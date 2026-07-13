from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []  # in-memory list, resets when app restarts — fine for now


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    #if not data or "title" not in data:
    #    return jsonify({"error": "title is required"}), 400
    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
