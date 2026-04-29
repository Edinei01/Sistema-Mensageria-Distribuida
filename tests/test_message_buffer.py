import unittest
from src.client import Client
from src.message_buffer import MessageBuffer


class TestMessageBuffer(unittest.TestCase):

    # Inicializa o ambiente de teste criando buffer e clientes
    def setUp(self):
        self.buffer = MessageBuffer()
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    # Testa se o buffer adiciona mensagens corretamente e mantém ordem Lamport
    def test_add_and_order(self):
        m1 = self.alice.send("msg1", receiver=self.bob)
        m2 = self.alice.send("msg2", receiver=self.bob)

        self.buffer.add(m2)
        self.buffer.add(m1)

        self.assertEqual(
            self.buffer._MessageBuffer__buffer[0].timestamp,
            1
        )

    # Testa se deliver marca mensagens como entregues corretamente
    def test_deliver_marks_messages(self):
        msg = self.alice.send("oi", receiver=self.bob)

        self.buffer.add(msg)
        self.buffer.deliver()

        self.assertIn(msg.message_id, self.buffer._MessageBuffer__delivered)

    # Testa filtragem de mensagens por cliente (sender ou receiver)
    def test_get_by_client(self):
        msg = self.alice.send("oi", receiver=self.bob)
        self.buffer.add(msg)

        result = self.buffer.get_by_client(self.bob)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], msg)

    # Testa retorno correto do status do buffer
    def test_status(self):
        msg = self.alice.send("oi", receiver=self.bob)
        self.buffer.add(msg)

        status = self.buffer.status()

        self.assertEqual(status["buffer_size"], 1)


if __name__ == "__main__":
    unittest.main()