"""====Remove Duplicates from Sorted List =====
"""
num = [1, 1, 2, 3, 3]
ans = [1, 2, 3]

""" ====Using LInked List....."""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


""" 
1 --> 1 --> 2 --> 3 --> 3

ans = 1 --> 2 -->3
"""
head = ListNode(1)
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(3)

head.next = A
A.next = B
B.next = C
C.next = D


def display(head):
    cur = head
    element = []
    while cur:
        element.append(str(cur.val))
        cur = cur.next
    return " -->".join(element)


def deleteDuplicate(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next  # skip the duplicate value
        else:
            cur = cur.next
    return head


new_head = deleteDuplicate(head)

print(
    f'Original array {display(head)}---After remove Duplicate: {display(new_head)}')
