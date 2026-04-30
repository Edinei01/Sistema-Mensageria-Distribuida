import unittest
from src.client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.alice = Client("Alice")
        self.bob = Client("Bob")

    def test_clock_logic(self):
        msg = self.alice.send("Oi")

        # Pegamos apenas o segundo elemento do retorno (o número)
        new_t = self.bob.receive(msg)[1]

        print(f"Tempo extraído: {new_t}")
        self.assertEqual(new_t, 2)
        self.assertEqual(self.bob.clock.time, 2)