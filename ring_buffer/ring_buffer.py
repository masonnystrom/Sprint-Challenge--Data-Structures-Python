class RingBuffer:
    """essentially snakes the list"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.current = 0 # holds oldest value 

    def append(self, item):
        # add item to list if list is not at capacity
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.current +=1
        else:
            # the current item with new item
            self.storage[self.current] = item
            # # divided by the capacity to return remainder
            self.current = ((self.current+1) % self.capacity)

    def get(self):
        buffer_list = []
        for x in self.storage:
            if x is not None:
                buffer_list.append(x)
        return buffer_list
