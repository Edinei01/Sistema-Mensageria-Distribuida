import unittest
from src.channel import Channel
from src.client import Client

class TestChannel(unittest.TestCase):
    def setUp(self):
        self.channel = Channel("devs")
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_broadcast_distribution(self):
        self.channel.join(self.alice)
        self.channel.join(self.bob)

        msg = self.alice.send("Olá grupo", channel="devs")
        delivered = self.channel.distribute(msg)

        self.assertEqual(len(delivered), 1)
        self.assertEqual(delivered[0].receiver.name, "Bob")