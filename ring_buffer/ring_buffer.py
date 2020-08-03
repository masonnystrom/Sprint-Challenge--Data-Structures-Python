from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    """essentially snakes the list"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            # assign head
            self.current = self.storage.head
        else: # list is at or greater than capacity
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if self.storage.head == self.current:
                self.current =  self.storage.tail


    def get(self):
        list_buffer = []
        
        # starting point for list
        first_node = self.current
        list_buffer.append(first_node.value)
        if first_node.next:
            next_node = first_node.next
        else:
            next_node = self.storage.head
        
        while next_node != first_node:
            list_buffer.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head
        return list_buffer
