import base64
from src.crypto.symmetric import SymmetricCrypto
from src.crypto.asymmetric import AsymmetricCrypto


class PGP:
    @staticmethod
    def encrypt_message(content: str, target_public_key):
        """
        1. Gera chave simétrica única.
        2. Cifra conteúdo com AES.
        3. Cifra chave AES com RSA pública.
        """
        # Passo 1: Chave de sessão efêmera[cite: 26]
        session_key = SymmetricCrypto.generate_key()
        sym_cipher = SymmetricCrypto(session_key)

        # Passo 2: Cifragem simétrica[cite: 26]
        encrypted_data = sym_cipher.encrypt(content)

        # Passo 3: Cifragem assimétrica da chave[cite: 24]
        asym_helper = AsymmetricCrypto()
        encrypted_session_key = asym_helper.encrypt_with_public(target_public_key, session_key)

        return {
            "session_key": base64.b64encode(encrypted_session_key).decode('utf-8'),
            "data": encrypted_data
        }

    @staticmethod
    def decrypt_message(payload, recipient_asym_engine):
        """
        1. Recupera a chave AES com a RSA privada.
        2. Abre a mensagem com a chave AES.
        """
        enc_key = base64.b64decode(payload['session_key'])

        # Recupera chave simétrica original[cite: 24]
        session_key = recipient_asym_engine.decrypt_with_private(enc_key)

        # Descriptografa a mensagem final[cite: 26]
        sym_cipher = SymmetricCrypto(session_key)
        return sym_cipher.decrypt(payload['data'])














# import hmac
# import hashlib
#
#
# class PGP:
#
#     def __init__(self, secret_key: str):
#         self.secret_key = secret_key.encode()
#
#     def sign_message(self, content: str):
#         signature = hmac.new(
#             self.secret_key,
#             content.encode(),
#             hashlib.sha256
#         ).hexdigest()
#         return signature
#
#     def verify_signature(self, content: str, received_signature: str):
#         expected_signature = hmac.new(
#             self.secret_key,
#             content.encode(),
#             hashlib.sha256
#         ).hexdigest()
#
#         return hmac.compare_digest(expected_signature, received_signature)