# ==================== Heaps and Priority Queues =============

# 1. Min Heap (Heapify)
# Time O(n), space O(1)

from collections import Counter
import heapq
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
heapq.heapify(A)  # ceating the heap ...heapq.heapify(Arr)

heapq.heappush(A, 400)  # appedning an element
print(A)

min = heapq.heappop(A)  # pop the smallest

print(A)

# find the 3 largest elelments
maxi = heapq.nlargest(3, A)
print(f"3 largest elements: {maxi}")

# find the 3 smallest elements
mini = heapq.nsmallest(3, A)
print(f"3 smallest elements: ", mini)

# heap pop (extract min value) # time is O(log n)
minn = heapq.heappop(A)
print(minn)

# heap sort : O(nlog n) and space O(n)


def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list


print("\n ==== Heap sorting ====")
print(heapsort(A))

print("\n")
print("============= Max Heap ============")
# Max Heap
B = [-4, 3, 1, 0, 2, 5, 11, 8, 9, 14, 2, 3, 7, -3]
print(f"origial B: {B}")
n = len(B)
for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print(B)
largest = -heapq.heappop(B)
print(f"largest value is {largest}")


print("======Peak at Min: O(1)")
print(f"min: {B[0]}")


# pushing into heap
print("\n ================ Heap PUsh =================")
c = [-5, 6, 7, 2, 3, 5, 1, 0]
heap = []
for x in c:
    heapq.heappush(heap, x)
    print(heap)
# def maxA(A):
#     maxA = A[0]
#     minA = A[0]
#     for i in A:
#         if i >= maxA:
#             maxA = i
#         if i <= minA:
#             minA = i
#     return [maxA, minA]

# print("Max and Min Number are ", maxA(A))


# puting tuples of items on the heap
print("\n ============== tuple of itmes on the heap ==================")
D = [5, 4, 3, 4, 3, 5, 5, 4]
# counter = Counter(D)

# print(f"Counter is : {counter}")

# looping thruogh the ocunter


def topKfreq(arr, k):
    counter = Counter(arr)
    heap = []
    for num, freq in counter.items():
        print(f"key, freq: {num, freq}")
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    num = [num for freq, num in heap]
    print(f"Array: {arr}")
    return num


print(f"My heap: {heap}")
print("lenght: ", len(heap))

print(topKfreq(D, 3))
