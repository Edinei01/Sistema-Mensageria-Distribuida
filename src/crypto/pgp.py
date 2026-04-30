import hmac
import hashlib


class PGP:

    def __init__(self, secret_key: str):
        self.secret_key = secret_key.encode()

    def sign_message(self, content: str):
        signature = hmac.new(
            self.secret_key,
            content.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def verify_signature(self, content: str, received_signature: str):
        expected_signature = hmac.new(
            self.secret_key,
            content.encode(),
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(expected_signature, received_signature)