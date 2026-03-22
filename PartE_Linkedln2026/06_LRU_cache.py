""" 
    ==========LRU = Least Recently Used:======
  ---If the cache is full and you need to add a new item:
  ---remove the item that was used the longest time ago
  
  e.g, input
  ["LRUCache", "put", "put", "get", "put", "get", "get", "get"]
  [[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
  
  Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
  
  Could you do get and put on O(1) time complexity?
"""


class Node:
    def __init__(self, key, val):
        pass


class LRUCache:

    def __init__(self, capacity: int):
        pass

    # pointer functions to remove and insert
    def remove(self, node):
        pass

    def insert(self, node):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
