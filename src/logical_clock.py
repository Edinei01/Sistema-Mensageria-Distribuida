class LogicalClock:

    # construtor
    def __init__(self):
        self.__time = 0

    # getter
    @property
    def clock(self) -> int:
        return self.__time

    # setter
    @clock.setter
    def clock(self, new_time: int) -> None:
        self.__time = new_time

    # método interno para incrementar o tempo
    def __increment(self) -> None:
        self.__time += 1

    # registra um evento local ou de envio e retorna o tempo atual
    def send_tick(self) -> int:
        self.__increment()
        return self.clock

    # sincroniza o relógio com um tempo recebido e incrementa
    def receive_tick(self, received_time: int) -> None:
        # atualiza o tempo comparando com o valor recebido
        self.clock = max(self.clock, received_time)
        self.__increment()
