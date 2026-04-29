from typing import Optional
from uuid import uuid4
from src.client import Client


class Message:

    def __init__(
        self,
        sender: Client,
        content: str,
        timestamp: int,
        receiver: Optional[Client] = None,
        channel: Optional[str] = None
    ) -> None:

        if receiver is not None and channel is not None:
            raise ValueError("Message não pode ter receiver e channel ao mesmo tempo")

        self.__sender = sender
        self.__content = content
        self.__timestamp = timestamp
        self.__receiver = receiver
        self.__channel = channel
        self.__encrypted = False
        self.__message_id = str(uuid4())

    # GETTERS
    @property
    def sender(self) -> Client:
        return self.__sender

    @property
    def content(self) -> str:
        return self.__content

    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @property
    def receiver(self) -> Optional[Client]:
        return self.__receiver

    @property
    def channel(self) -> Optional[str]:
        return self.__channel

    @property
    def encrypted(self) -> bool:
        return self.__encrypted

    @property
    def message_id(self) -> str:
        return self.__message_id

    # SETTER
    @encrypted.setter
    def encrypted(self, value: bool) -> None:
        self.__encrypted = value

    # MÉTODOS DE ESTADO
    def mark_as_encrypted(self) -> None:
        self.__encrypted = True

    def mark_as_decrypted(self) -> None:
        self.__encrypted = False

    # LÓGICA DE REPRESENTAÇÃO
    def get_summary(self) -> str:
        if self.__receiver:
            destino = f"to {self.__receiver}"
        elif self.__channel:
            destino = f"channel {self.__channel}"
        else:
            destino = "broadcast"

        return (
            f"[{self.__timestamp}] "
            f"{self.__sender} -> {destino}: "
            f"{self.__content} "
            f"(encrypted={self.__encrypted})"
        )

    def __str__(self) -> str:
        return self.get_summary()