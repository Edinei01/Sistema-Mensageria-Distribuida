from uuid import uuid4

class Message:
    def __init__(self, sender, content, timestamp, receiver=None, channel=None):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp
        self.receiver = receiver
        self.channel = channel
        self.id = str(uuid4())