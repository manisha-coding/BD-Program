from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id = 1


# Add a task
@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id

    data = request.get_json()

    task = {
        "id": task_id,
        "title": data["title"],
        "status": data["status"]
    }

    tasks.append(task)
    task_id += 1

    return jsonify(task), 201


# View all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)