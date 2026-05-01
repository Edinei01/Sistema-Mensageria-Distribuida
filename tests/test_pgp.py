import unittest
from src.crypto.pgp import PGP
from src.crypto.asymmetric import AsymmetricCrypto


class TestPGPCrypto(unittest.TestCase):
    def setUp(self):
        self.destinatario_asym = AsymmetricCrypto()
        self.mensagem = "Mensagem altamente confidencial"

    def test_hybrid_encryption_structure(self):
        payload = PGP.encrypt_message(self.mensagem, self.destinatario_asym.public_key)

        self.assertIsInstance(payload, dict)
        self.assertIn("session_key", payload)
        self.assertIn("data", payload)
        self.assertNotEqual(payload["data"], self.mensagem)

    def test_full_decryption_flow(self):
        payload = PGP.encrypt_message(self.mensagem, self.destinatario_asym.public_key)

        mensagem_recuperada = PGP.decrypt_message(payload, self.destinatario_asym)

        self.assertEqual(mensagem_recuperada, self.mensagem)

    def test_decryption_fails_with_wrong_private_key(self):
        payload = PGP.encrypt_message(self.mensagem, self.destinatario_asym.public_key)

        hacker_asym = AsymmetricCrypto()

        with self.assertRaises(Exception):
            PGP.decrypt_message(payload, hacker_asym)


if __name__ == '__main__':
    unittest.main()