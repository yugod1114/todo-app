import json
from datetime import datetime


class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_from_file()

    def add_task(self, description):
        self.tasks.append({
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    def show_tasks(self):
        if not self.tasks:
            print("\n📭 当前没有任务")
            return

        print("\n📝 任务列表:")
        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task["completed"] else "⏳"
            print(f"{i}. [{status}] {task['description']}")
            print(f"   📅 创建: {task['created_at']}")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print("🎉 任务已完成！")
        else:
            print("❌ 无效的任务编号")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            # 重新编号
            for i, task in enumerate(self.tasks, 1):
                task["id"] = i
            print(f"🗑️ 已删除任务: {removed['description']}")
        else:
            print("❌ 无效的任务编号")

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(self.tasks, f, indent=2)