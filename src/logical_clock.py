class LogicalClock:

    def __init__(self) -> None:
        self.__time = 0

    @property
    def time(self) -> int:
        return self.__time

    # evento local (envio)
    def send_tick(self) -> int:
        self.__time += 1
        return self.__time

    # evento de recebimento (sincronização Lamport)
    def receive_tick(self, received_time: int) -> int:
        self.__time = max(self.__time, received_time) + 1
        return self.__time