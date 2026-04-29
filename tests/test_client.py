import unittest
from src.client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_clock_logic(self):
        msg = self.alice.send("Oi")
        self.assertEqual(self.alice.clock.time, 1)

        new_t = self.bob.receive(msg)
        self.assertEqual(new_t, 2)
        self.assertEqual(self.bob.clock.time, 2)