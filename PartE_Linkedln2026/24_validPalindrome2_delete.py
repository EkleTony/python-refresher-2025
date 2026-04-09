""" 
======Valid Palindrome II - LeetCode 680 - 


======Step-by-Step Approach (Clear Flow)
1. Use two pointers (left, right) to scan from both ends of the string.
2. While characters match, keep moving inward.
3. When a mismatch happens, you are allowed one deletion.
4. Use a helper function to check:
5. If skipping the left character makes it a palindrome
6. OR skipping the right character makes it a palindrome
7. If either case is valid → return True.
8. If no mismatch occurs → the string is already a palindrome 

→ return True.===="""


def validPalindrome2(st):
    # using two pointer apporch

    # step 1: helper function to check if substring is s[l:r] if palindrome
    def is_pal(left, right):
        while left < right:
            if st[left] != st[right]:
                return False
                left += 1
                right -= 1
            return True

    # initialize two ponters
    left = 0
    right = len(st) - 1
    # traverse inward while left pointer is befoer reight pointer
    while left < right:
        if st[left] != st[right]:
            # skip or delete the left or right char...!
            return is_pal(left+1, right) or is_pal(left, right-1)

        left += 1
        right -= 1
    return True
