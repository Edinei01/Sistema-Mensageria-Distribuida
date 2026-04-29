from typing import Set, List
from src.client import Client
from src.message import Message


class Channel:

    def __init__(self, name: str) -> None:
        # nome lógico do canal (ex: "dev-team")
        self.__name = name

        # membros conectados ao canal
        self.__members: Set[Client] = set()

        # histórico opcional de mensagens (útil pra debug/teste)
        self.__messages: List[Message] = []

    # retorna nome do canal
    @property
    def name(self) -> str:
        return self.__name

    # adiciona cliente ao canal
    def join(self, client: Client) -> None:
        self.__members.add(client)

    # remove cliente do canal
    def leave(self, client: Client) -> None:
        self.__members.discard(client)

    # verifica se cliente pertence ao canal
    def has_member(self, client: Client) -> bool:
        return client in self.__members

    # envia mensagem para todos os membros do canal
    def broadcast(self, message: Message) -> List[Message]:
        delivered = []

        for member in self.__members:
            if member != message.sender:
                msg_copy = Message(
                    sender=message.sender,
                    content=message.content,
                    timestamp=message.timestamp,
                    receiver=member,
                    channel= None
                )
                delivered.append(msg_copy)

        self.__messages.append(message)
        return delivered

    # retorna histórico do canal
    @property
    def messages(self) -> List[Message]:
        return self.__messages

    # string do canal
    def __str__(self) -> str:
        return f"Channel({self.__name}, members={len(self.__members)})"