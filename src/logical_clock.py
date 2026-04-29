class LogicalClock:
    def __init__(self):
        self.__time = 0

    @property
    def time(self):
        return self.__time

    def send_tick(self):
        self.__time += 1
        return self.__time

    def receive_tick(self, received_time):
        self.__time = max(self.__time, received_time) + 1
        return self.__time