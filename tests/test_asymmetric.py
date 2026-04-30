import unittest
from src.crypto.asymmetric import AsymmetricCrypto


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.crypto = AsymmetricCrypto()

    def test_key_generation(self):
        self.assertIsNotNone(self.crypto.public_key)
        self.assertIsNotNone(self.crypto.private_key)

    def test_encryption_decryption(self):
        original_msg = "Mensagem secreta 123"

        encrypted = self.crypto.encrypt_with_public(self.crypto.public_key, original_msg)

        self.assertIsNotNone(encrypted)
        self.assertNotEqual(original_msg, encrypted)

        decrypted = self.crypto.decrypt_with_private(encrypted)

        self.assertEqual(original_msg, decrypted)

    def test_encryption_fails_with_wrong_key(self):
        other_crypto = AsymmetricCrypto()
        msg = "Dados sensíveis"

        encrypted = other_crypto.encrypt_with_public(other_crypto.public_key, msg)

        with self.assertRaises(Exception):
            self.crypto.decrypt_with_private(encrypted)

if __name__ == '__main__':
    unittest.main()
