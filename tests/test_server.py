import unittest
from src.server import Server
from src.client import Client


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = Server()

        self.alice = Client("Alice")
        self.bob = Client("Bob")
        self.peter = Client("Peter")

        self.channel = self.server.create_channel("dev-team")
        self.channel.join(self.bob)
        self.channel.join(self.peter)

    # testa roteamento unicast
    def test_unicast_routing(self):
        msg = self.alice.send("oi bob", receiver=self.bob)

        self.server.route(msg)

        status = self.server.status()

        self.assertEqual(status["buffer_size"], 1)

    # testa multicast via canal
    def test_multicast_routing(self):
        msg = self.alice.send("oi time", channel="dev-team")

        self.server.route(msg)

        status = self.server.status()

        self.assertEqual(status["buffer_size"], 2)

    # testa broadcast
    def test_broadcast_routing(self):
        msg = self.alice.send("oi geral")

        self.server.route(msg)

        status = self.server.status()

        self.assertEqual(status["buffer_size"], 1)

    # testa entrega geral
    def test_delivery(self):
        msg = self.alice.send("oi")

        self.server.route(msg)
        self.server.deliver()

        status = self.server.status()

        self.assertGreaterEqual(status["delivered_size"], 1)


if __name__ == "__main__":
    unittest.main()