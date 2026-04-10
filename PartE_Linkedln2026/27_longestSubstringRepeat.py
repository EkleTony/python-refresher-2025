""" Longest Substring Without Repeating Characters - Leetcode 3 - Python


"""
st = "abcabcdef"
# max_len = 3


def longestSubstring(st):
    # a b c a b c d d
    # 0 1 2 3 4 5 6 7
    # idea: is to use a sliding window.
    charSet = set()
    max_len = 0
    left = 0

    for right in range(len(st)):
        while st[right] in charSet:
            charSet.remove(st[left])
            left += 1
        charSet.add(st[right])
        # sliding window
        window = (right - left) + 1
        max_len = max(max_len, window)
    return max_len


st = "abcabcbb"

print(f"Longest Substring of {st} is == {longestSubstring(st)}")


""" ========== Return the Strings too= ===="""


def longestStringPartB(st):
    charset = set()
    left = 0
    max_len = 0
    # introduce start
    start = left
    for right in range(len(st)):
        while st[right] in charset:
            charset.remove(st[left])
            left += 1

        charset.add(st[right])

        # ======“If I need the substring, I’ll store the start index when I update max length.”
        window = (right - left) + 1
        if window > max_len:
            max_len = right - left + 1
            start = left
        # max_len = max(max_len, window)
    return max_len, st[start: start+max_len]


print(
    f"Longest Substring and return B=== of {st} is == {longestStringPartB(st)}")
