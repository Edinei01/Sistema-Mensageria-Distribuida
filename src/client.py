from src.logical_clock import LogicalClock
from src.crypto.asymmetric import AsymmetricCrypto
from src.crypto.pgp import PGP


class Client:
    def __init__(self, name: str):
        self.name = name
        self.clock = LogicalClock()
        self.asym_engine = AsymmetricCrypto()
        self.public_keys_directory = {}

    def get_my_public_key(self):
        return self.asym_engine.public_key

    def save_public_key(self, name, key):
        self.public_keys_directory[name] = key

    def send(self, content: str, receiver=None, channel=None):
        payload = content

        if receiver and receiver.name in self.public_keys_directory:
            payload = PGP.encrypt_message(content, self.public_keys_directory[receiver.name])

        from src.message import Message  #
        t = self.clock.send_tick()
        return Message(self, payload, t, receiver, channel)

    def receive(self, message):
        content_to_show = message.content

        if isinstance(message.content, dict) and "session_key" in message.content:
            try:
                content_to_show = PGP.decrypt_message(message.content, self.asym_engine)
            except Exception:
                content_to_show = "[ERRO PGP: Falha na decriptografia]"

        new_t = self.clock.receive_tick(message.timestamp)
        return content_to_show, new_t