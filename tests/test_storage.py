import unittest
import os
import tempfile
from task_manager.storage import load_tasks, save_tasks
from task_manager.models import Task


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.temp_dir.cleanup()

    def test_save_and_load_tasks(self):
        tasks = [
            Task(1, "Persisted Task"),
            Task(2, "Another Task", priority=1)
        ]

        save_tasks(tasks)
        loaded = load_tasks()

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].title, "Persisted Task")
        self.assertEqual(loaded[1].priority, 1)


if __name__ == "__main__":
    unittest.main()
