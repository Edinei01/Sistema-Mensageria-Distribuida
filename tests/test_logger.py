import unittest
import os
from src.logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        self.log_file = os.path.join(self.log_dir, "log_conferencia.txt")

        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_file_creation(self):
        Logger.log_event("TEST", "Alice", 1)
        self.assertTrue(os.path.exists(self.log_file))