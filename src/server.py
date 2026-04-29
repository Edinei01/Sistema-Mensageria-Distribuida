from src.message_buffer import MessageBuffer
from src.logger import Logger
from src.channel import Channel


class Server:
    def __init__(self):
        self.buffer = MessageBuffer()
        self.channels = {}

    def create_channel(self, name):
        if name not in self.channels:
            self.channels[name] = Channel(name)
        return self.channels[name]

    def route(self, msg):
        mode = "UNICAST"
        if msg.channel:
            mode = "BROADCAST" if msg.channel == "geral" else "MULTICAST"

        Logger.log_event(f"{mode}_SEND", msg.sender.name, msg.timestamp, info=msg.content)

        if msg.channel and msg.channel in self.channels:
            for sub_msg in self.channels[msg.channel].distribute(msg):
                self.buffer.add(sub_msg)
        else:
            self.buffer.add(msg)

    def process(self):
        for msg in self.buffer.get_pending():
            if msg.receiver:
                new_t = msg.receiver.receive(msg)
                Logger.log_event("CONSUMED", msg.sender.name, msg.timestamp,
                                 msg.receiver.name, new_t, msg.content)
            self.buffer.mark_done(msg.id)