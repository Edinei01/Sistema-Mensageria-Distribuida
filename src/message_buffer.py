from typing import Optional, List, Set
from src.message import Message


class MessageBuffer:

    # Inicializa o buffer de mensagens, controle de entregas e limite de capacidade
    def __init__(self, max_size: Optional[int] = None) -> None:
        self.__buffer: List[Message] = []
        self.__delivered: Set[str] = set()
        self.__max_size = max_size

    # Adiciona uma nova mensagem ao buffer e mantém ordenação Lamport
    def add(self, message: Message) -> None:
        self.__buffer.append(message)
        self.__sort_buffer()

        if self.__max_size is not None and len(self.__buffer) > self.__max_size:
            self.__enforce_capacity()

    # Ordena o buffer por timestamp Lamport, depois por sender e message_id
    def __sort_buffer(self) -> None:
        self.__buffer.sort(
            key=lambda m: (
                m.timestamp,
                m.sender.name,
                m.message_id
            )
        )

    # Remove mensagens antigas quando o buffer ultrapassa a capacidade máxima
    def __enforce_capacity(self) -> None:
        while len(self.__buffer) > self.__max_size:
            self.__buffer.pop(0)

    # Entrega mensagens que ainda não foram processadas e marca como entregues
    def deliver(self) -> None:
        for message in self.__buffer:
            if message.message_id not in self.__delivered:
                print(f"[DELIVERED] {message}")
                self.__delivered.add(message.message_id)

    # Retorna todas as mensagens associadas a um cliente (sender ou receiver)
    def get_by_client(self, client) -> List[Message]:
        return [
            m for m in self.__buffer
            if m.sender == client or m.receiver == client
        ]

    # Retorna todas as mensagens de um determinado canal (multicast)
    def get_by_channel(self, channel: str) -> List[Message]:
        return [
            m for m in self.__buffer
            if m.channel == channel
        ]

    # Remove mensagens já entregues, limpando o buffer
    def clean(self) -> None:
        self.__buffer = [
            m for m in self.__buffer
            if m.message_id not in self.__delivered
        ]

    # Retorna informações gerais do estado atual do buffer
    def status(self) -> dict:
        return {
            "buffer_size": len(self.__buffer),
            "delivered_size": len(self.__delivered),
            "max_size": self.__max_size
        }