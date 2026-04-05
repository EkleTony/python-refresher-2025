""" Valid Palindrome - Leetcode 125 - 2 Pointers (Python)
 """

st = "race a car"
st1 = "aba"


def validPalindrome(st):
    # 1. lower case, 2. check for isalnum() and 3. reverese check
    lst = []
    st = st.lower()
    for ch in st:
        if ch.isalnum():  # Filter only alphanumeric characters.
            lst.append(ch)
    return lst[::1] == lst[::-1]  # reverse


""" 
1.Start pointers at both ends.
2. Skip non-alphanumeric characters.
3. Compare lowercase characters.
4. If mismatch → return False.
5. Move both pointers inward.
6.vIf loop ends → return True."""
# O(n) and O(n)


def validPalindrome_optimal(st):
    # using two pointers
    left = 0
    right = len(st) - 1
    while left < right:
        if not st[left].isalnum():
            left += 1
            continue
        if not st[right].isalnum():
            right -= 1
            continue
        # compare lowercase characters
        if st[left].lower() != st[right].lower():
            return False
        left += 1
        right -= 1
    return True


print(f' is {st} Valid palindrome? {validPalindrome(st)} ')
print()
print(f' is {st} Valid palindrome? {validPalindrome(st1)} ')
print("")
print(f' is {st} Valid palindrome? {validPalindrome_optimal(st1)} ')
