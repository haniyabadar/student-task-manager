import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tasks import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.m = TaskManager()

    def test_add_task(self):
        t = self.m.add_task("Study DevOps")
        self.assertEqual(t["title"], "Study DevOps")
        self.assertEqual(len(self.m.list_tasks()), 1)

    def test_complete_task(self):
        t = self.m.add_task("Lab")
        self.m.complete_task(t["id"])
        self.assertTrue(self.m.list_tasks()[0]["done"])

    def test_delete_task(self):
        t = self.m.add_task("Temp")
        self.m.delete_task(t["id"])
        self.assertEqual(self.m.list_tasks(), [])

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.m.add_task("   ")


if __name__ == "__main__":
    unittest.main()