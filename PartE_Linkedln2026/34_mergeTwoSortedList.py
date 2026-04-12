"""=====	Merge Two Sorted Lists ======
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list

"""

# ===== USing Linked-List...!!!!
lst2 = [[1, 2, 3], [1, 3, 4]]
ans = [1, 1, 2, 3, 4, 4]


def mergedList(lists):
    merged = []
    for lst in lists:
        merged.extend(lst)

    merged.sort()
    return merged


print(f'Merging list {lst2} is ===  {mergedList(lst2)}')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergedList(list1, list2):
    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next

        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next
    # update remaingig nodes
    cur.next = list1 if list1 else list2
    return dummy.next


def display(head):
    cur = head
    element = []
    while cur:
        element.append(str(cur.val))
        cur = cur.next
    return "--> ".join(element)


# examples
list1 = ListNode(1)
A = ListNode(2)
B = ListNode(4)
list1.next = A
A.next = B

# list2
list2 = ListNode(1)
A2 = ListNode(3)
B2 = ListNode(4)
list2.next = A2
A2.next = B2

print("============ Display my List======")
print(f'List1 = {display(list1)}')
print(f'List2 = {display(list2)}')

mergedList = mergedList(list1, list2)

print(f'Merged list is ==  {display(mergedList)} ')
