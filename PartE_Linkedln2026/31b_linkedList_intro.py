"""  ======= Singly LInked List and Double LInked list ==============
     ================================================================

---Singly Linked List (SLL): Each node contains data and a single pointer to the next node.
             It can only be traversed in the forward direction.

---Doubly Linked List (DLL): Each node contains data, a next pointer, and a previous pointer. 
             This allows for bidirectional traversal (forward and backward). 

Nodes:  (head)  A --> B --> C --> null  (tail)
Pointers:       1     2     3

==== adding nodes====
Class Node:
    node.value
    node.next # ref to differenc obj
"""


class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# make a link list
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print("Head", Head)

"""Traversing the List -- O(n)"""
print("=======Traversing the Link list=======")
curr = Head
while curr:
    print(curr)
    curr = curr.next

print("\n ========= PART 1:  Display Single LInnked list======= O(n)")


def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    return " --> ".join(element)


Head2 = SinglyNode(3)
A2 = SinglyNode(5)
B2 = SinglyNode(12)
C2 = SinglyNode(33)
D2 = SinglyNode(9)

Head2.next = A2
A2.next = B2
B2.next = C2
C2.next = D2

print(f'Linked List: {display(Head2)} \n')


""" ======= Searching for node values ============ O(n)"""


print("\n ===========Searching for Node Values ====== ")


def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        else:
            curr = curr.next
    return False


print(f"Searching for node 10: {search(Head2, 10)}")


print("\n ========= PART 2:  Display Double LInnked list ======= O(n)")


class DoubleNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


head_dll = tail_dll = DoubleNode(1)
print("tail is ", tail_dll)


def diplayDLL(head, tail):
    curr = head
    prev = tail
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(" < --> ".join(element))


def insert_at_begin(head, tail, val):
    new_node = DoubleNode(val, next=head)
    head.prev = new_node
    return new_node, tail

def insert_at_end(head, tail, val):
    new_node = DoubleNode(val, prev = tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_begin(head_dll, tail_dll, 3)
diplayDLL(head, tail)

head2, tail2 = insert_at_end(head, tail, 7)
diplayDLL(head2, tail2)
