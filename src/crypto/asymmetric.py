from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization


class AsymmetricCrypto:
    def __init__(self):
        # Gera o par de chaves RSA[cite: 24]
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

    def get_public_key_bytes(self):
        # Correção: o nome correto do método é public_bytes[cite: 8, 24]
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def encrypt_with_public(self, public_key, data):
        # Garante que os dados sejam bytes[cite: 24]
        if isinstance(data, str):
            data = data.encode()

        # Uso obrigatório de AsymmetricPadding (OAEP)[cite: 24]
        return public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt_with_private(self, encrypted_data):
        # Descriptografia com a chave privada[cite: 24]
        return self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )









# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from cryptography.hazmat.primitives import serialization
#
# class AsymmetricCrypto:
#     def __init__(self):
#         self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
#         self.public_key = self.private_key.public_key()
#
#     def get_public_key_bytes(self):
#         return self.public_key.public_serialization(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PublicFormat.SubjectPublicKeyInfo
#         )
#
#     def encrypt_with_public(self, public_key, data: str):
#         return public_key.encrypt(
#             data.encode(),
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#
#     def decrypt_with_private(self, encrypted_data):
#         return self.private_key.decrypt(
#             encrypted_data,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         ).decode()