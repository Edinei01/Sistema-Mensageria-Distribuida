import unittest
from src.message import Message


# Mock simples de Client (evita depender da implementação real)
class FakeClient:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class TestMessage(unittest.TestCase):

    def setUp(self):
        self.alice = FakeClient("Alice")
        self.bob = FakeClient("Bob")

    # Teste: criação de mensagem unicast
    def test_create_unicast_message(self):
        msg = Message(
            sender=self.alice,
            content="Oi Bob",
            timestamp=1,
            receiver=self.bob
        )

        self.assertEqual(msg.sender, self.alice)
        self.assertEqual(msg.receiver, self.bob)
        self.assertIsNone(msg.channel)
        self.assertEqual(msg.timestamp, 1)
        self.assertFalse(msg.encrypted)

    # Teste: criação de multicast
    def test_create_multicast_message(self):
        msg = Message(
            sender=self.alice,
            content="Oi grupo",
            timestamp=2,
            channel="dev-team"
        )

        self.assertEqual(msg.channel, "dev-team")
        self.assertIsNone(msg.receiver)

    # Teste: broadcast
    def test_create_broadcast_message(self):
        msg = Message(
            sender=self.alice,
            content="Oi geral",
            timestamp=3
        )

        self.assertIsNone(msg.receiver)
        self.assertIsNone(msg.channel)

    # Teste: erro ao passar receiver e channel juntos
    def test_invalid_message(self):
        with self.assertRaises(ValueError):
            Message(
                sender=self.alice,
                content="Erro",
                timestamp=1,
                receiver=self.bob,
                channel="dev-team"
            )

    # Teste: criptografia
    def test_encryption_flag(self):
        msg = Message(
            sender=self.alice,
            content="Oi Bob",
            timestamp=1,
            receiver=self.bob
        )

        msg.mark_as_encrypted()
        self.assertTrue(msg.encrypted)

        msg.mark_as_decrypted()
        self.assertFalse(msg.encrypted)

    # Teste: summary (unicast)
    def test_summary_unicast(self):
        msg = Message(
            sender=self.alice,
            content="Oi Bob",
            timestamp=1,
            receiver=self.bob
        )

        summary = msg.get_summary()

        self.assertIn("Alice", summary)
        self.assertIn("Bob", summary)
        self.assertIn("Oi Bob", summary)
        self.assertIn("[1]", summary)

    # Teste: summary broadcast
    def test_summary_broadcast(self):
        msg = Message(
            sender=self.alice,
            content="Oi geral",
            timestamp=3
        )

        summary = msg.get_summary()

        self.assertIn("broadcast", summary)


if __name__ == '__main__':
    unittest.main()