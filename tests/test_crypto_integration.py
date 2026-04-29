import unittest
from src.client import Client
from src.crypto.symmetric import SymmetricCrypto


class TestCryptoIntegration(unittest.TestCase):
    def setUp(self):
        self.shared_key = SymmetricCrypto.generate_key()

        self.alice = Client("Alice")
        self.bob = Client("Bob")

        self.alice.set_key(self.shared_key)
        self.bob.set_key(self.shared_key)

    def test_end_to_end_encryption(self):
        original_text = "Mensagem Ultra Secreta"

        msg = self.alice.send(original_text, receiver=self.bob)

        self.assertNotEqual(msg.content, original_text)
        print(f"\nTexto Criptografado no Buffer: {msg.content}")

        decrypted_text, _ = self.bob.receive(msg)

        self.assertEqual(decrypted_text, original_text)
        print(f"Texto Decifrado pelo Bob: {decrypted_text}")

    def test_fail_with_wrong_key(self):
        msg = self.alice.send("Segredo", receiver=self.bob)

        hacker = Client("Hacker")
        hacker.set_key(SymmetricCrypto.generate_key())

        result, _ = hacker.receive(msg)
        self.assertIn("ERRO", result)
        print(f"Resultado do Hacker: {result}")


if __name__ == '__main__':
    unittest.main()