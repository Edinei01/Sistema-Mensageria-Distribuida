class MessageBuffer:
    def __init__(self):
        self.__queue = []
        self.__delivered_ids = set()

    def add(self, message):
        if message.id not in self.__delivered_ids:
            self.__queue.append(message)
            self.__queue.sort(key=lambda m: (m.timestamp, m.sender.name))

    def get_pending(self):
        return [m for m in self.__queue if m.id not in self.__delivered_ids]

    def mark_done(self, msg_id):
        self.__delivered_ids.add(msg_id)