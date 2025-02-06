import unittest

# Simple To-Do List class
class ToDoList:
    def __init__(self):  # Corrected 'init' to '__init__'
        self.tasks = []

    def add_task(self, task):
        if not task.strip():
            return "Error: Task cannot be empty"
        self.tasks.append(task)
        return self.tasks

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return self.tasks
        return "Error: Task not found"

# Test Cases
class TestToDoList(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.todo = ToDoList()

    def test_add_task(self):
        """TC001: Add a single task"""
        result = self.todo.add_task("Buy groceries")
        self.assertEqual(result, ["Buy groceries"])

    def test_add_multiple_tasks(self):
        """TC002: Add multiple tasks"""
        self.todo.add_task("Do homework")
        self.todo.add_task("Go to gym")
        self.assertEqual(self.todo.tasks, ["Do homework", "Go to gym"])

    def test_add_empty_task(self):
        """TC003: Add an empty task"""
        result = self.todo.add_task("")
        self.assertEqual(result, "Error: Task cannot be empty")

    def test_delete_task(self):
        """TC004: Delete a task"""
        self.todo.add_task("Read a book")
        result = self.todo.delete_task("Read a book")
        self.assertEqual(result, [])

    def test_delete_all_tasks(self):
        """TC005: Delete all tasks"""
        self.todo.add_task("Cook dinner")
        self.todo.add_task("Exercise")
        self.todo.delete_task("Cook dinner")
        self.todo.delete_task("Exercise")
        self.assertEqual(self.todo.tasks, [])

    def test_delete_non_existent_task(self):
        """TC006: Try to delete a non-existent task"""
        result = self.todo.delete_task("Non-existent task")
        self.assertEqual(result, "Error: Task not found")

if __name__ == "__main__":  # Corrected 'main' to '__main__'
    unittest.main()
