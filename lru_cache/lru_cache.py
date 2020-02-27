"""
LRU CACHE
"""

from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the storage.
    """

    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the storage.
    """

    def get(self, key):
        if key in self.storage:
            val = self.storage[key].value
            self.list.move_to_front(self.storage[key])
            self.storage[key] = self.storage.pop(key)
            return val[1]
        return None

    """
    Adds the given key-value pair to the storage. The newly-
    added pair should be considered the most-recently used
    entry in the storage. If the storage is already at max capacity
    before this entry is added, then the oldest entry in the
    storage needs to be removed to make room. Additionally, in the
    case that the key already exists in the storage, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        """
        Put to storage
        """
        node = (key, value)
        if key in self.storage:
            self.storage[key].value = node
            return
        if self.size < self.limit:
            self.size += 1
            self.storage[key] = self.list.add_to_head(node)
            return
        self.storage[key] = self.list.add_to_head(node)
        self.storage.pop(self.list.tail.value[0])
        self.list.remove_from_tail()

