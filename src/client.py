from src.logical_clock import LogicalClock
from src.crypto.symmetric import SymmetricCrypto


class Client:
    def __init__(self, name: str):
        self.name = name
        self.clock = LogicalClock()
        self.key = None

    def set_key(self, key: bytes):
        self.key = key

    def send(self, content: str, receiver=None, channel=None):
        if self.key:
            crypto = SymmetricCrypto(self.key)
            content = crypto.encrypt(content)

        from src.message import Message
        t = self.clock.send_tick()
        return Message(self, content, t, receiver, channel)

    def receive(self, message):
        content_to_show = message.content
        if self.key:
            try:
                crypto = SymmetricCrypto(self.key)
                content_to_show = crypto.decrypt(message.content)
            except Exception:
                content_to_show = "[ERRO: Não foi possível decifrar a mensagem]"

        new_t = self.clock.receive_tick(message.timestamp)

        return content_to_show, new_t