class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        self.storage.append(item)
        if len(self.storage) == self.capacity:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.storage

    class __Full:
        def append(self, x):
            self.storage[self.cur] = x
            self.cur = (self.cur+1) % self.capacity

        def get(self):
            return self.storage