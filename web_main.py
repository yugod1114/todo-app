from flask import Flask, render_template, request, jsonify, redirect, url_for
from todo import TodoManager
import os

app = Flask(__name__)
todo = TodoManager(filename="web_tasks.json")  # 使用独立数据文件避免冲突


@app.route('/')
def index():
    tasks = todo.get_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    if title:
        todo.add_task(title)
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    todo.complete_task(task_id)
    return jsonify(success=True)


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    todo.delete_task(task_id)
    return jsonify(success=True)


if __name__ == '__main__':
    # 创建 templates 文件夹和 HTML 文件
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # 自动生成 HTML 模板（首次运行时）
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write("""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌐 Web Todo 应用</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #f8f9fa; padding: 20px; }
        .task-card { margin-bottom: 15px; transition: all 0.2s; }
        .task-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .completed { text-decoration: line-through; opacity: 0.7; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">📝 Todo Web 应用</h1>

        <!-- 添加任务表单 -->
        <div class="card mb-4">
            <div class="card-body">
                <form action="/add" method="POST">
                    <div class="input-group">
                        <input type="text" name="title" class="form-control" placeholder="输入新任务..." required maxlength="100">
                        <button type="submit" class="btn btn-primary">添加</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- 任务列表 -->
        <div class="row">
            {% for task in tasks %}
            <div class="col-md-6 mb-3">
                <div class="card task-card {% if task.done %}border-success{% else %}border-primary{% endif %}">
                    <div class="card-body d-flex justify-content-between align-items-center">
                        <div>
                            <h5 class="card-title {% if task.done %}completed text-success{% endif %}">
                                {{ task.title }}
                            </h5>
                            <p class="text-muted small mb-0">
                                ID: {{ task.id }} | 创建于 {{ task.created_at }}
                            </p>
                        </div>
                        <div>
                            {% if not task.done %}
                            <form action="/complete/{{ task.id }}" method="POST" class="d-inline">
                                <button type="submit" class="btn btn-sm btn-success me-1">完成</button>
                            </form>
                            {% endif %}
                            <form action="/delete/{{ task.id }}" method="POST" class="d-inline">
                                <button type="submit" class="btn btn-sm btn-danger">删除</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
        """)

    print("\n✅ 服务已启动: http://127.0.0.1:5000")
    app.run(debug=True)