import unittest
from datetime import date
from task_manager.models import Task
from task_manager.exceptions import InvalidTaskError


class TestTaskModel(unittest.TestCase):

    def test_valid_task_creation(self):
        task = Task(1, "Test Task", priority=2)
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

    def test_empty_title_raises_error(self):
        with self.assertRaises(InvalidTaskError):
            Task(1, "")

    def test_invalid_priority_raises_error(self):
        with self.assertRaises(InvalidTaskError):
            Task(1, "Bad priority", priority=10)

    def test_due_date_assignment(self):
        d = date.today()
        task = Task(1, "With due", due_date=d)
        self.assertEqual(task.due_date, d)


if __name__ == "__main__":
    unittest.main()
