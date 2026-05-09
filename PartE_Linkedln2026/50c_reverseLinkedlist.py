""" ========== Reversing Linked list"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head, next=None):
        new_node = Node(head)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def append(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

    def reverse(self):
        # step 1--switch head and tail
        # temp = head and then head == tial and then tail = tem
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # two more pointers... b4 temp and after temp
        # before--> temp-->after

        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            # before<--temp  after-->
            before = temp
            # before<--temp  after-->
            # ====== (before == temp   after--->)
            temp = after
            # (before <---temp   after--->)

    def display(self):
        curr = self.head
        element = []
        while curr:
            element.append(str(curr.value))
            curr = curr.next
        return "-->".join(element)


new_linkedlist = LinkedList(2)
new_linkedlist.append(3)
new_linkedlist.append(23)
print(f"====Display the Linkedlist====")
print(f"Current Linkedlist: {new_linkedlist.display()}")
new_linkedlist.reverse()

print(f"Reversed Linkedlist: {new_linkedlist.display()}")
