import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from todo import TodoManager
import threading


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Todo 应用 - Windows 风格")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # 初始化数据
        self.todo = TodoManager()
        self.tasks = []

        # 创建界面
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # 顶部操作栏
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x")

        ttk.Button(top_frame, text="➕ 添加任务", command=self.add_task).pack(side="left", padx=5)
        ttk.Button(top_frame, text="✅ 完成任务", command=self.complete_task).pack(side="left", padx=5)
        ttk.Button(top_frame, text="🗑️ 删除任务", command=self.delete_task).pack(side="left", padx=5)

        # 任务列表
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "任务", "状态", "创建时间"),
            show="headings",
            height=15
        )

        # 设置列宽
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("任务", width=250)
        self.tree.column("状态", width=80, anchor="center")
        self.tree.column("创建时间", width=150, anchor="center")

        # 添加表头
        for col in ("ID", "任务", "状态", "创建时间"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # 双击编辑任务
        self.tree.bind("<Double-1>", self.edit_task)

    def load_tasks(self):
        """加载并显示任务"""
        # 清空现有数据
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.tasks = self.todo.get_tasks()
        for task in self.tasks:
            status = "已完成" if task["done"] else "进行中"
            self.tree.insert("", "end",
                             values=(task["id"], task["title"], status, task["created_at"]),
                             tags=("done" if task["done"] else "pending")
                             )

        # 设置行颜色
        self.tree.tag_configure("done", background="#e6ffed")
        self.tree.tag_configure("pending", background="#fffbe6")

    def add_task(self):
        title = simpledialog.askstring("添加任务", "请输入任务内容:")
        if title and title.strip():
            self.todo.add_task(title.strip())
            self.load_tasks()

    def complete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("警告", "请先选择一个任务")
            return

        task_id = self.tree.item(selected[0])["values"][0]
        self.todo.complete_task(task_id)
        self.load_tasks()

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("警告", "请先选择一个任务")
            return

        task_id = self.tree.item(selected[0])["values"][0]
        if messagebox.askyesno("确认", f"确定要删除任务 {task_id} 吗？"):
            self.todo.delete_task(task_id)
            self.load_tasks()

    def edit_task(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        task_id = self.tree.item(selected[0])["values"][0]
        new_title = simpledialog.askstring("编辑任务", "修改任务内容:",
                                           initialvalue=self.tree.item(selected[0])["values"][1])

        if new_title and new_title.strip():
            for task in self.tasks:
                if task["id"] == task_id:
                    task["title"] = new_title.strip()
                    self.todo.save_tasks()  # 直接保存修改
                    self.load_tasks()
                    break


if __name__ == "__main__":
    root = tk.Tk()
    # 设置 Windows 风格主题
    style = ttk.Style()
    style.theme_use('vista' if 'vista' in style.theme_names() else 'winnative')

    app = TodoApp(root)
    root.mainloop()