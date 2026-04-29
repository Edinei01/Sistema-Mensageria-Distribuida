import unittest
from src.message import Message
from src.client import Client

class TestMessage(unittest.TestCase):

    def setUp(self):
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_create_unicast_message(self):
        msg = Message(
            sender=self.alice,
            content="Oi Bob",
            timestamp=1,
            receiver=self.bob
        )

        self.assertEqual(msg.sender, self.alice)
        self.assertEqual(msg.receiver, self.bob)
        self.assertEqual(msg.content, "Oi Bob")
        self.assertEqual(msg.timestamp, 1)
        self.assertIsNone(msg.channel)
        self.assertTrue(len(msg.id) > 0)

    def test_create_multicast_message(self):
        msg = Message(
            sender=self.alice,
            content="Oi grupo",
            timestamp=2,
            channel="dev-team"
        )

        self.assertEqual(msg.channel, "dev-team")
        self.assertIsNone(msg.receiver)

    def test_create_broadcast_message(self):
        msg = Message(
            sender=self.alice,
            content="Oi geral",
            timestamp=3
        )

        self.assertIsNone(msg.receiver)
        self.assertIsNone(msg.channel)

    def test_message_string_representation(self):

        msg = Message(self.alice, "Teste", 10, receiver=self.bob)
        self.assertIsNotNone(str(msg))

if __name__ == '__main__':
    unittest.main()