import unittest
from src.todo import TodoList


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()
        self.todo.tasks = []  # 重置测试状态

    def test_add_task(self):
        self.todo.add_task("学习Git")
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]["description"], "学习Git")

    def test_complete_task(self):
        self.todo.add_task("测试任务")
        self.todo.complete_task(1)
        self.assertTrue(self.todo.tasks[0]["completed"])

    def test_delete_task(self):
        self.todo.add_task("任务1")
        self.todo.add_task("任务2")
        self.todo.delete_task(1)
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]["description"], "任务2")


if __name__ == "__main__":
    unittest.main()