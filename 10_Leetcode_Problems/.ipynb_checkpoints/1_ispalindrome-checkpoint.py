# Leetcode 125 Valid palindrome
"""   ============ 125. Valid Palindrome ============
1. Given a string s, return if it's a palindrome True or False

A phrase is a palindrome if,
 -- after converting all uppercase letters into lowercase letters,
 -- and removing all non-alphanumeric characters, it reads the same forward and backward.
 -- Alphanumeric characters include letters and numbers.
    """


def is_palindrome(test):
    # 1. lowercase
    test = test.lower()

    lst = []
    for char in test:
        if char.isalnum():
            lst.append(char)

    newstr = ''.join(lst)
    print(newstr)
    return newstr[::1] == newstr[::-1]


# Examples
test_word1 = "bab"
test_word2 = "hellow worlds my friend"

print(f"test1: {is_palindrome(test_word1)}")
print(f"test 2: {is_palindrome(test_word2)}")
