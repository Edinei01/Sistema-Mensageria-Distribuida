import unittest
from src.crypto.pgp import PGP


class TestPGPCrypto(unittest.TestCase):
    def setUp(self):
        self.secret_key = "chave_mestra_secreta"
        self.pgp = PGP(self.secret_key)
        self.mensagem = "Mensagem importante"

    def test_signature_generation(self):
        assinatura = self.pgp.sign_message(self.mensagem)
        self.assertIsInstance(assinatura, str)
        self.assertEqual(len(assinatura), 64)

    def test_valid_signature(self):
        assinatura = self.pgp.sign_message(self.mensagem)
        resultado = self.pgp.verify_signature(self.mensagem, assinatura)
        self.assertTrue(resultado, "A assinatura deveria ser válida para a mensagem original")

    def test_invalid_signature_content_changed(self):
        assinatura = self.pgp.sign_message(self.mensagem)

        mensagem_adulterada = "Mensagem importantej"

        resultado = self.pgp.verify_signature(mensagem_adulterada, assinatura)
        self.assertFalse(resultado, "A assinatura não deveria ser válida se o conteúdo mudou")

    def test_invalid_signature_wrong_key(self):
        pgp_hacker = PGP("outra_chave_qualquer")
        assinatura_falsa = pgp_hacker.sign_message(self.mensagem)

        resultado = self.pgp.verify_signature(self.mensagem, assinatura_falsa)
        self.assertFalse(resultado, "A assinatura feita com chave diferente deve ser rejeitada")


if __name__ == '__main__':
    unittest.main()