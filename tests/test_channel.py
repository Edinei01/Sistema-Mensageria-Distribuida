import unittest
from src.channel import Channel
from src.client import Client


class TestChannel(unittest.TestCase):

    def setUp(self):
        self.channel = Channel("dev-team")

        self.alice = Client("Alice")
        self.bob = Client("Bob")
        self.peter = Client("Peter")

    # testa entrada de membros no canal
    def test_join_channel(self):
        self.channel.join(self.alice)

        self.assertTrue(self.channel.has_member(self.alice))

    # testa saída de membros do canal
    def test_leave_channel(self):
        self.channel.join(self.alice)
        self.channel.leave(self.alice)

        self.assertFalse(self.channel.has_member(self.alice))

    # testa broadcast para múltiplos membros
    def test_broadcast(self):
        self.channel.join(self.alice)
        self.channel.join(self.bob)
        self.channel.join(self.peter)

        msg = self.alice.send("oi time", channel="dev-team")

        delivered = self.channel.broadcast(msg)

        # Alice não deve receber sua própria mensagem
        self.assertEqual(len(delivered), 2)

        # cada membro recebe uma cópia
        receivers = [m.receiver.name for m in delivered]
        self.assertIn("Bob", receivers)
        self.assertIn("Peter", receivers)

    # testa histórico do canal
    def test_history(self):
        self.channel.join(self.alice)

        msg = self.alice.send("mensagem 1", channel="dev-team")

        self.channel.broadcast(msg)

        self.assertEqual(len(self.channel.messages), 1)


if __name__ == "__main__":
    unittest.main()