from typing import List, Optional
from src.message import Message
from src.message_buffer import MessageBuffer
from src.channel import Channel
from src.client import Client


class Server:

    def __init__(self) -> None:
        # buffer central de mensagens (ordenação + entrega)
        self.__buffer = MessageBuffer()

        # canais registrados no servidor
        self.__channels: dict[str, Channel] = {}

    # registra canal no servidor
    def create_channel(self, name: str) -> Channel:
        channel = Channel(name)
        self.__channels[name] = channel
        return channel

    # retorna canal existente
    def get_channel(self, name: str) -> Optional[Channel]:
        return self.__channels.get(name)

    # entrada única do sistema (core do servidor)
    def route(self, message: Message) -> None:
        if message.receiver is not None:
            self.__send_unicast(message)

        elif message.channel is not None:
            self.__send_multicast(message)

        else:
            self.__send_broadcast(message)

    # entrega 1 para 1
    def __send_unicast(self, message: Message) -> None:
        self.__buffer.add(message)

    # entrega para canal
    def __send_multicast(self, message: Message) -> None:
        channel = self.__channels.get(message.channel)

        if not channel:
            raise ValueError(f"Canal {message.channel} não existe")

        delivered = channel.broadcast(message)

        for msg in delivered:
            self.__buffer.add(msg)

    # entrega para todos os canais e clientes conhecidos
    def __send_broadcast(self, message: Message) -> None:
        self.__buffer.add(message)

    # entrega final (simulação de rede)
    def deliver(self) -> None:
        self.__buffer.deliver()

    # status do sistema
    def status(self) -> dict:
        return self.__buffer.status()