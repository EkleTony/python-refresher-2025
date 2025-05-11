# Find the longest string in a list of strings

# input = ["hello", "worlds", "this is a string"]
# result = 16

# ==========method 1 ==============
def find_largest(numbers):
    n = len(numbers)
    result = []
    for st in numbers:
        result.append(len(st))
    return max(result)


def find_largest2(numbers):
    maxlen = 0
    for s in numbers:
        if len(s) > maxlen:
            maxlen = len(s)
    return maxlen


# Test case!
test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]

print()
print(test_strings)
print(f"\n Largest String: {find_largest(test_strings)}")
print(f"Method 2: largest string: {find_largest2(test_strings)} ")
