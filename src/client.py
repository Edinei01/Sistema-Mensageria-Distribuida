from src.logical_clock import LogicalClock
from src.message import Message

class Client:

    def __init__(self, name: str):
        self.__name = name
        self.__clock = LogicalClock()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def clock(self) -> LogicalClock:
        return self.__clock

    # SEND
    def send(self, content: str, receiver=None, channel=None) -> Message:
        timestamp = self.__clock.send_tick()

        print(f"[SEND] {self.__name} clock={timestamp}")

        return Message(
            sender=self,
            content=content,
            timestamp=timestamp,
            receiver=receiver,
            channel=channel
        )

    # RECEIVE
    def receive(self, message: Message) -> None:
        self.__clock.receive_tick(message.timestamp)

        print(f"[RECEIVED] {self.__name} clock={self.__clock.time} | {message}")

    def __str__(self) -> str:
        return self.__name