import unittest
from src.channel import Channel
from src.client import Client


class TestChannel(unittest.TestCase):
    def setUp(self):
        self.channel = Channel("dev-team")
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_distribute(self):
        self.channel.join(self.alice)
        self.channel.join(self.bob)

        msg = self.alice.send("oi time", channel="dev-team")
        delivered = self.channel.distribute(msg)

        self.assertEqual(len(delivered), 1)
        self.assertEqual(delivered[0].receiver.name, "Bob")