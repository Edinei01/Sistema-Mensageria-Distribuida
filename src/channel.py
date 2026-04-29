class Channel:
    def __init__(self, name):
        self.name = name
        self.members = []

    def join(self, client):
        if client not in self.members:
            self.members.append(client)

    def distribute(self, msg):
        from src.message import Message
        return [Message(msg.sender, msg.content, msg.timestamp, receiver=m) 
                for m in self.members if m != msg.sender]