import json
import os
from datetime import datetime


class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """从文件加载任务"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """保存任务到文件"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def add_task(self, title):
        """添加新任务"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ 已添加任务: {title}")

    def show_tasks(self):
        """显示所有任务"""
        if not self.tasks:
            print("📭 你的任务列表是空的！")
            return

        print("\n📝 当前任务列表:")
        print("-" * 50)
        for task in self.tasks:
            status = "✅" if task["done"] else "⏳"
            print(f"ID: {task['id']} [{status}] {task['title']} (创建于: {task['created_at']})")
        print("-" * 50)

    def complete_task(self, task_id):
        """标记任务为完成"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save_tasks()
                print(f"🎉 任务 {task_id} 已完成！")
                return
        print("❌ 未找到该任务 ID")

    def delete_task(self, task_id):
        """删除任务"""
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < initial_length:
            # 重新编号
            for i, task in enumerate(self.tasks, 1):
                task["id"] = i
            self.save_tasks()
            print(f"🗑️ 任务 {task_id} 已删除")
        else:
            print("❌ 未找到该任务 ID")