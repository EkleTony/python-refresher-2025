"""_summary_ leetcode 771----

Q: How many stones are jewels....



e.r, input== jewels = "aA", stones = "aAAbbbb"

output = 3 i.e first three char are jewels... aAA

"""

jewels = "aA"
stones = "aAAbbbb"

# -===== USING HASHING METHODS====


def jewelStone(jewels, stones):
    # using hashing set(a, A)---O(n+m)
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count
    # this is actually O(n^2)


def jewelStone_set(jewels, stones):
    s = set(jewels)  # hasing i,e, ("a", "A", ....) #O(m)
    count = 0

    for stone in stones:  # O(n)
        if stone in s:  # O(1)
            count += 1
    return count


print("lenght of jewel in stones:", jewelStone_set( jewels, stones))
