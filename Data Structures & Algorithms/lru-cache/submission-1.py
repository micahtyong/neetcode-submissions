# To keep track of LRU, use a doubly linked list (access order)
#   - Stack would not be O(1) (e.g., deleting then re-inserting)
#   - When used, move to front of list (via sentinel)
#   - fixed size hashmap for O(1) get. delete is O(1)
#   - for simplicity, on get operations, just remove from list, then add it back
#   - hashmap should have pointer to node

# lru_sentinel <-> 1 <-> mru_sentinel 
# sentinel -> 2 -> 1
# sentinel -> 3 -> 2 -> 1 

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None # lru
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {} # { key: (value, node_pointer)}
        self.front_sentinel = Node(None) # mru
        self.last_sentinel = Node(None) # lru

        self.front_sentinel.next = self.last_sentinel
        self.last_sentinel.prev = self.front_sentinel

        self.capacity = capacity

    def _insert_at_front(self, node: Node):
        prev_next = self.front_sentinel.next
        
        self.front_sentinel.next = node
        node.prev = self.front_sentinel
        node.next = prev_next
        prev_next.prev = node
    
    # Assume: node is already in linked list
    def _dereference(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None
    
    # Assume: Never will be called if no elements (e.g., capacity >= 1)
    def _evict(self):
        lru_element = self.last_sentinel.prev
        self._dereference(lru_element)
        del self.d[lru_element.val]
        pass

    def get(self, key: int) -> int:
        # Gets value + node pointer
        if key not in self.d:
            return -1

        val, node_pointer = self.d[key]
        self._dereference(node_pointer)
        self._insert_at_front(node_pointer)
        return val

    def put(self, key: int, value: int) -> None:
        # Duplicate key, just update value
        if key in self.d:
            _, node_pointer = self.d[key]
            self.d[key] = (value, node_pointer) 
            # then you also have to update again
            self._dereference(node_pointer)
            self._insert_at_front(node_pointer)
            return

        node = Node(key)
        self.d[key] = (value, node) 
        self._insert_at_front(node)
        if len(self.d) > self.capacity:
            self._evict()


