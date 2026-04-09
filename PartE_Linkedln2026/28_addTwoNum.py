

def addTwoNumber(l1, l2):
    # carry bit and digit
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry

        # next digit and caryy
        carry = total//10  # e.g, 6+6 =12, 2 carry 1
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
