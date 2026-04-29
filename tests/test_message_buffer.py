import unittest
from src.client import Client
from src.message_buffer import MessageBuffer


class TestMessageBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = MessageBuffer()
        self.alice = Client("Alice")

    def test_order_by_timestamp(self):
        m1 = self.alice.send("primeira")
        m2 = self.alice.send("segunda")

        self.buffer.add(m2)
        self.buffer.add(m1)

        pending = self.buffer.get_pending()

        self.assertEqual(pending[0].timestamp, 1)
        self.assertEqual(pending[1].timestamp, 2)