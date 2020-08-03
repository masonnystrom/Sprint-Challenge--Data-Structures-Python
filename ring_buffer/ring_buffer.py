class RingBuffer:
    """essentially snakes the list"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.current = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.current +=1
        else:
            self.storage[self.current] = item
            self.current = ((self.current+1) % self.capacity)

    def get(self):
        buffer_list = []
        for x in self.storage:
            if x is not None:
                buffer_list.append(x)
        return buffer_list
