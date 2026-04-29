import unittest
from src.client import Client
from src.message_buffer import MessageBuffer


class TestMessageBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = MessageBuffer()
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_add_and_order(self):
        m1 = self.alice.send("msg1", receiver=self.bob)
        m2 = self.alice.send("msg2", receiver=self.bob)
        self.buffer.add(m2)
        self.buffer.add(m1)

        pending = self.buffer.get_pending()
        self.assertEqual(pending[0].timestamp, 1)
        self.assertEqual(pending[1].timestamp, 2)

    def test_mark_done(self):
        msg = self.alice.send("oi", receiver=self.bob)
        self.buffer.add(msg)
        self.buffer.mark_done(msg.id)
        self.assertEqual(len(self.buffer.get_pending()), 0)