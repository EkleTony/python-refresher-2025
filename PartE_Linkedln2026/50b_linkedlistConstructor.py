class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return self.value

    def display(self):
        curr = self.head
        element = []
        while curr is not None:
            element.append(str(curr.value))
            curr = curr.next
        return "--->".join(element)

    def append(self, value):
        self.value = Node(value)

        if self.head == None:
            self.head = self.value
            self.tail = self.value
        else:
            self.tail.next = self.value
            self.tail = self.value
        self.length += 1
        # optional ---> using becus we will need it to call on the append method later..
        return True

    def pop(self):
        curr = self.head
        prev = curr
        # case 1--- no element
        if self.head == None:
            print("Stack underflow...!")
            return None

        prev = self.head
        temp = self.head
        # case2--- one node
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        # case 3---if more than two elements

        while temp.next:
            prev = temp
            temp = temp.next

        # deletion happens here
        self.tail = prev
        self.tail.next = None
        self.length -= 1

        # # Case3: if only one node
        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = None

    def prepend(self, value):
        # create a node
        self.value = Node(value)

        # case1: if empty...!
        if self.head == None:
            self.head = self.value
            self.tail = self.value
        else:
            self.value.next = self.head
            self.head = self.value
        self.length += 1

        return True

    def popfirst(self):
        # case1== no item
        if self.head is None:
            return None

        temp = self.head
        # case 2: if one item
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        curr = self.head

        # ---method 1--- uisng while loop
        # count = 0
        # while curr:
        #     if index == count:
        #         return curr.value

        #     curr = curr.next
        #     count += 1
        # return None

        # -==== method 2 Using For --loop
        for _ in range(index):
            curr = curr.next
        return curr  # or curr.value

    def set_value(self, index, value):
        # case 1.. if empty
        if index < 0 or index >= self.length:
            return None
        # cass 2--- if not empty
        curr = self.head

        # 33=== using our get mehtod
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

        # === ======Using for loop
        # for _ in range(index):
        #     curr = curr.next
        # curr.value = value
        # return True

        # ====Usiing while loop
        # count = 0
        # while curr:
        #     if index == count:
        #         curr.value = value
        #     curr = curr.next
        #     count += 1
        # return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        # case 2==if index 0
        if index == 0:
            return self.prepend(value)
        # case 3== if index at end
        if index == self.length:
            return self.append(value)
        # if index at middle...!

        # helper function to get index
        def get_node(index):
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        # geting the previous index..before the position to add
        new_node = Node(value)
        prev = get_node(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        # case 1--- if empty or out of range
        if index < 0 or index >= self.length:
            return None  # ---- because if successful return a node... rlse none..!
        # if index is 0 or end

        def popfirst2():
            curr = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head = None
            self.length -= 1
            return curr
            # if more than 1

        def pop2():

            if self.length == 1:
                self.head = None
                self.tail = None
            prev = self.head
            temp = self.head

            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1

        if index == 0:
            return popfirst2()
        if index == self.length-1:
            return pop2()

        # now at middle
        def get_node(index):
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        prev = get_node(index - 1) # O(n)
        temp = prev.next  # get_node(index) 
        prev.next = temp.next
        temp.next = None
        self.length -= 1


double_linkedlist = LinkedList(400)

print(f"One lenght LL: ==  head --> {double_linkedlist.head.value}")
# A = DoubleLL(6)
# B = DoubleLL(10)


# def display(head):
#     curr = head
#     element = []
#     while curr is not None:
#         element.append(str(curr.value))
#         curr = curr.next
#     return "==>".join(element)


# Connect NODES, not linked list objects
# double_linkedlist.append(23)
# double_linkedlist.append(5)
print(f"Printing LinkedLIst: = {double_linkedlist.display()}")
print("\n ==== Appending and POPPING to Linked list=====")
double_linkedlist.append(13)
double_linkedlist.append(10)
print(f"Before Pop: = {double_linkedlist.display()}")

double_linkedlist.pop()
print(f"After Pop: = {double_linkedlist.display()}")

double_linkedlist.pop()
print(
    f"After Pop again---lenght is  = {double_linkedlist.display()}")

double_linkedlist.pop()
print(
    f"After Pop again---lenght is  = {double_linkedlist.display()}")

double_linkedlist.prepend("A")
print(f"After Prepend  = {double_linkedlist.display()}")
double_linkedlist.append(12)
double_linkedlist.append(14)
print(
    f"After appendind  = {double_linkedlist.display()}")
double_linkedlist.popfirst()
print(
    f"After PopFirst  = {double_linkedlist.display()}")
double_linkedlist.append(140)
double_linkedlist.append(1)
print(f"current LL: {double_linkedlist.display()}")
print(f"Get value in index 2 : {double_linkedlist.get(3)}")
print("\n======Setting Values=======")
double_linkedlist.set_value(2, 1000)
print(f"Setting index 2 value : {double_linkedlist.display()}")

print("\n========INSERTING==========")
double_linkedlist.insert(1, 3000)
print(
    f"After Inserting 3000 at index 3==== {double_linkedlist.insert(1, 6000)}")
print(f"Setting index 2 value : {double_linkedlist.display()}")

new_linkedlist = LinkedList(0)
new_linkedlist.insert(1, 1)
new_linkedlist.append(5)
new_linkedlist.prepend(67)
new_linkedlist.pop()
print(f"Display linkedlist: {new_linkedlist.display()}")
