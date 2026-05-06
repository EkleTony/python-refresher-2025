""" === SEction 2==== Classes and Pointers=====  """

dict1 = {"value": 2}
dict2 = dict1

dict2["value"] = 4

print(f" dict 1: {dict1} and points to: {id(dict1)}")
print(f" dict 2: {dict2} and points to: {id(dict2)}")

"""Note: Dictionary can be changed while integers are immutable...!

---> Keep note of this concept, like in LInkedList if we have two varaiable that points to 
a node...even if we change it.. still points to same location."""

"""==========LInked list=========

.... head --> (11) --> (3) --> (23) --> (7) --> tail


=====Linked list under the hood...!

"""

head = {"value": 11,
        "next": {
            "value": 3,
            "next": {
                "value": 23,
                "next": {
                    "value": 7,
                    "next": None
                }
            }
        }

        }

print(f"Linked list: {head}")
print(head['next']['next']['next']["value"])


class NodeList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


my_listedlist = NodeList(11)
A = NodeList(3)
B = NodeList(23)
C = NodeList(7)

my_listedlist.next = A
A.next = B
B.next = C

print(my_listedlist)

# =======Displaying the linked list


def display(head):
    curr = head
    element = ["head"]
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    return "-->".join(element)


print(f"LInkedlist = {display(my_listedlist)}")
