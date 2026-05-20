from todo import TodoList
from utils import clear_screen


def show_menu():
    print("\n===== 待办事项管理器 =====")
    print("1. 添加任务")
    print("2. 查看所有任务")
    print("3. 标记任务完成")
    print("4. 删除任务")
    print("5. 退出")
    return input("请选择操作: ")


def main():
    todo = TodoList()
    while True:
        clear_screen()
        choice = show_menu()

        if choice == "1":
            task = input("\n请输入任务内容: ")
            todo.add_task(task)
            print("✅ 任务已添加！")

        elif choice == "2":
            todo.show_tasks()

        elif choice == "3":
            todo.show_tasks()
            try:
                idx = int(input("输入要完成的任务编号: "))
                todo.complete_task(idx)
            except ValueError:
                print("❌ 请输入有效编号！")

        elif choice == "4":
            todo.show_tasks()
            try:
                idx = int(input("输入要删除的任务编号: "))
                todo.delete_task(idx)
            except ValueError:
                print("❌ 请输入有效编号！")

        elif choice == "5":
            print("\n💾 正在保存数据...")
            todo.save_to_file()
            print("👋 退出程序，再见！")
            break

        input("\n按回车键继续...")


if __name__ == "__main__":
    main()