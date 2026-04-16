""" Leetcode 141--- LInked lIst cycel

---given head, the head of a linked list, determine if the linked list has a cycle in it.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(self, head):
    dummy = ListNode()
    dummy.next = head
    # two pointers
    slow = fast = dummy

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            return True
    return False


head3 = ListNode(3)
A = ListNode(2)
B = ListNode(0)
C = ListNode(-4)

head3.next = A
A.next = B
B.next = C
C.next = A


def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    return " --> ".join(element)


print(f'Linked List: {display(head3)} \n')
