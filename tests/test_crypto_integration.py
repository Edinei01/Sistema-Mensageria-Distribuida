import unittest
from src.client import Client


class TestCryptoIntegration(unittest.TestCase):
    def setUp(self):
        self.alice = Client("Alice")
        self.bob = Client("Bob")

        self.alice.save_public_key("Bob", self.bob.get_my_public_key())
        self.bob.save_public_key("Alice", self.alice.get_my_public_key())

    def test_end_to_end_encryption(self):
        original_text = "Mensagem Ultra Secreta"

        msg = self.alice.send(original_text, receiver=self.bob)

        self.assertIsInstance(msg.content, dict)
        self.assertNotEqual(msg.content, original_text)
        print(f"\nPayload PGP no Buffer: {msg.content}")

        decrypted_text, _ = self.bob.receive(msg)

        self.assertEqual(decrypted_text, original_text)
        print(f"Texto Decifrado pelo Bob: {decrypted_text}")

    def test_fail_with_wrong_key(self):
        msg = self.alice.send("Segredo", receiver=self.bob)

        hacker = Client("Hacker")

        result, _ = hacker.receive(msg)
        self.assertIn("ERRO", result)
        print(f"Resultado do Hacker: {result}")


if __name__ == '__main__':
    unittest.main()