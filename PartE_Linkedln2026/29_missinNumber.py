

def missingNum1(num):
    n = len(num) + 1
    expected = n*(n+1)//2
    actual = sum(num)
    missing = expected - actual
    return missing


print(f"missing num of {1, 2, 4, 5} is {missingNum1([1, 2, 4, 5])}")


def missingMultiple(num, k):
    seen = set(num)
    n = len(num) + k
    missing = []
    for i in range(1, n+1):
        if i not in seen:
            missing.append(i)
    return missing


print(f'Missing Numbers are in [1,3,4,6]: {missingMultiple([1, 2,3, 4, 6], 1)}')
