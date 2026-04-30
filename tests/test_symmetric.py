import unittest
from src.crypto.symmetric import SymmetricCrypto


class TestSymmetricCrypto(unittest.TestCase):

    def setUp(self):
        self.key = SymmetricCrypto.generate_key()
        self.crypto = SymmetricCrypto(self.key)

    def test_encryption_decryption(self):
        original_msg = "Mensagem secreta simétrica"

        encrypted = self.crypto.encrypt(original_msg)
        self.assertNotEqual(original_msg, encrypted)

        decrypted = self.crypto.decrypt(encrypted)
        self.assertEqual(original_msg, decrypted)

    def test_generate_key_is_valid(self):
        self.assertIsInstance(self.key, bytes)
        self.assertTrue(len(self.key) > 0)

    def test_decryption_with_wrong_key_fails(self):
        other_key = SymmetricCrypto.generate_key()
        other_crypto = SymmetricCrypto(other_key)

        msg = "Dados confidenciais"
        encrypted = self.crypto.encrypt(msg)

        with self.assertRaises(Exception):
            other_crypto.decrypt(encrypted)


if __name__ == '__main__':
    unittest.main()
