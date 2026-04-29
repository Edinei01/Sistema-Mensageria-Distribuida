import unittest
from src.server import Server
from src.client import Client


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = Server()
        self.alice = Client("Alice")
        self.bob = Client("Bob")

        self.channel = self.server.create_channel("dev-team")
        self.channel.join(self.alice)
        self.channel.join(self.bob)

    def test_unicast_routing_and_process(self):
        msg = self.alice.send("oi bob", receiver=self.bob)
        self.server.route(msg)

        self.assertEqual(len(self.server.buffer.get_pending()), 1)

        self.server.process()

        self.assertEqual(len(self.server.buffer.get_pending()), 0)