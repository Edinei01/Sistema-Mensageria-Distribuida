import unittest
from src.message import Message
from src.client import Client

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_create_message_attributes(self):
        msg = Message(self.alice, "Conteúdo", 1, receiver=self.bob)
        self.assertEqual(msg.sender, self.alice)
        self.assertEqual(msg.content, "Conteúdo")
        self.assertEqual(msg.timestamp, 1)
        self.assertEqual(msg.receiver, self.bob)
        self.assertIsNotNone(msg.id)