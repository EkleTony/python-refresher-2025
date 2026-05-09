"""=======Reverse Linked List - Leetcode 206 - Linked Lists (Python)

Gvien the head of a singly linked list, reverse the list and returnthe reversded list
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linkedlist:
    def __init__(self, head):
        new_node = Node(head)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # case 1 -- if empyt
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def display(self):
        curr = self.head
        element = []
        while curr is not None:
            element.append(str(curr.value))
            curr = curr.next
        return "-->".join(element)
    
    """========= `leetcode =---REversing....!"""
    def reverse(self):
        # case 1 if 1 node
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        # before --> temp -- > after
        while temp is not None:
            after = temp.next
            temp.next = before
            
            # before <-- temp   after --->
            before = temp
            temp = after

        
        # case  2 if multiple nodes


example1 = Linkedlist(1)
example1.append(2)
example1.append(3)
example1.append(4)
example1.append(5)

print(f"Single Linkedlist = {example1.display()}")
example1.reverse()
print(f"Reversing=== is  {example1.display()}")