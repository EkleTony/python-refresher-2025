""" Longest Substring Without Repeating Characters - Leetcode 3 - Python


"""
st = "abcabcdef"
# max_len = 3


def longestSubstring(st):
    char_set = set()
    left = 0
    max_subLenght = 0

    for right in range(len(st)):
        while st[left] in char_set:
            char_set.remove(st[left])
            left += 1

        char_set.add(st[right])
        window = (right - left) + 1
        max_subLenght = max(max_subLenght, right-left + 1)
    return max_subLenght


print(f"Longest Substring of {st} is == {longestSubstring(st)}")
