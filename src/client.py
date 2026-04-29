from src.logical_clock import LogicalClock

class Client:
    def __init__(self, name):
        self.name = name
        self.clock = LogicalClock()

    def send(self, content, receiver=None, channel=None):
        from src.message import Message
        t = self.clock.send_tick()
        return Message(self, content, t, receiver, channel)

    def receive(self, message):
        return self.clock.receive_tick(message.timestamp)