import unittest
from src.server import Server
from src.client import Client


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = Server()
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_unicast_flow(self):
        msg = self.alice.send("Oi Bob", receiver=self.bob)
        self.server.route(msg)

        self.server.process()

        self.assertEqual(len(self.server.buffer.get_pending()), 0)