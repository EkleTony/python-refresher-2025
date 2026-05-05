"""" LRU Cache------


1. Hash map
        This gives:
        fast lookup by key in O(1)
2. Doubly linked list
        This keeps items in usage order:
        most recently used at one end
        least recently used at the other end

IDEAS

“To design the LRU cache with O(1) operations,

1. I’ll use a combination of a HashMap and a doubly linked list.

--The HashMap will store key-to-node mappings for constant-time access.

--The doubly linked list will maintain the order of usage,
   where the most recently used items are near the head and the least recently used items are near the tail.

2. For the get operation, if the key exists, I retrieve the node,
move it to the front to mark it as recently used, and return its value. Otherwise, I return -1.

3. For the put operation, if the key already exists, I remove the old node.
   Then I insert the new node at the front. If the cache exceeds capacity,
   I remove the least recently used node from the tail.

I use a doubly linked list because it allows me to remove and insert nodes in constant time.”
"""


class ListNode:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


""" 
Inside the cache, keep:
        capacity
        cache = {} for key -> node
        dummy head and tail
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capcity = capacity
        self.cache = {}  # hashmpa for key ---> node

        # dummy nodes---
        self.head = ListNode()
        self.tail = ListNode()

        # connected the dummies to each other...
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove1(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.next = prev_node

        # A <--> node <--> B

    def insert(self, node):
        first_real_node = self.head.next

        node.next = first_real_node
        node.prev = self.head

        self.head.next = node
        first_real_node.prev = node

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def push(self, key: int, value: int):
        if key in self.cache:
            self.remove1(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        
        #checking
        if len(self.cache) > self.capcity:
            #remove lru and delete the lur from hashmap
            pass
