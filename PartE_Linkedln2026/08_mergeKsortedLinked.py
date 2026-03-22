"""  === Leetcode 23======

Q2: Merge k sorted lists

Given an anarray o fk liknked lists, list , each linnked-list is sorted in ascending order.

merge all the linnked-lists into on sorted linked-list and return it. 

"""
import heapq
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
output = [1, 1, 2, 3, 4, 4, 5, 6]


# ================== Soln 1===============
# =========================================
"""Easy solution for your current example
Since your input is a list of Python lists, the simplest way is:
1. put all numbers together
2. sort them
"""


def mergeKList_simple(lists):
    merged = []

    for lst in lists:
        merged.extend(lst)  # merging all list

    merged.sort()
    return merged  # return sorted list


print(f'Merge K sorted list: {mergeKList_simple(lists)}')


# =============linked-list solution using a heap===============
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    # Put the first node of each list into the heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)

        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
