from todo import TodoManager


def main():
    todo = TodoManager()

    while True:
        print("\n" + "=" * 40)
        print("      🐍 Python 待办事项练习版")
        print("=" * 40)
        print("1. 📥 添加任务")
        print("2. 👀 查看任务")
        print("3. ✅ 完成任务")
        print("4. 🗑️ 删除任务")
        print("5. 🚪 退出")

        choice = input("\n请选择一个操作 (1-5): ")

        if choice == "1":
            title = input("请输入任务内容: ")
            if title.strip():
                todo.add_task(title.strip())
            else:
                print("任务内容不能为空！")

        elif choice == "2":
            todo.show_tasks()

        elif choice == "3":
            todo.show_tasks()
            try:
                task_id = int(input("请输入要完成的任务 ID: "))
                todo.complete_task(task_id)
            except ValueError:
                print("请输入有效的数字 ID！")

        elif choice == "4":
            todo.show_tasks()
            try:
                task_id = int(input("请输入要删除的任务 ID: "))
                todo.delete_task(task_id)
            except ValueError:
                print("请输入有效的数字 ID！")

        elif choice == "5":
            print("👋 感谢使用，再见！")
            break

        else:
            print("❌ 无效选择，请重试。")


if __name__ == "__main__":
    main()