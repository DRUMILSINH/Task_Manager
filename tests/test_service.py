import unittest
from datetime import date, timedelta
from task_manager.service import TaskService
from task_manager.exceptions import TaskNotFoundError


class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.service = TaskService()

    def test_add_task(self):
        task = self.service.add_task("New Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(len(self.service.list_tasks()), 1)

    def test_mark_task_completed(self):
        task = self.service.add_task("Complete me")
        self.service.mark_task_completed(task.id)
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = self.service.add_task("Delete me")
        self.service.delete_task(task.id)
        self.assertEqual(len(self.service.list_tasks()), 0)

    def test_delete_nonexistent_task(self):
        with self.assertRaises(TaskNotFoundError):
            self.service.delete_task(999)

    def test_progress_calculation(self):
        self.service.add_task("A")
        self.service.add_task("B")
        self.service.mark_task_completed(1)
        self.assertEqual(self.service.get_progress(), 0.5)

    def test_overdue_tasks(self):
        yesterday = date.today() - timedelta(days=1)
        self.service.add_task("Late", due_date=yesterday)
        overdue = self.service.get_overdue_tasks(date.today())
        self.assertEqual(len(overdue), 1)


if __name__ == "__main__":
    unittest.main()
