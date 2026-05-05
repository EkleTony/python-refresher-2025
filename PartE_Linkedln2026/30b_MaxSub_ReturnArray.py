"""  Maximum Subarray - Amazon Coding Interview Question - Leetcode 53 - Python

"""


def maxSum1(num):
    # Using Kadanes Algorithm...
    """ The Kadane's algorithm is a linear time-- algorithm used to fing hte maximum sum of a contigous subarray
    ----Key Idea: is that at each index, we only need to track the maximum subarray ending at the index.

    Step1 : 
    1. Define the State: "I ain a variable current_sum, which represents the maximum subarray sum ending at the current index.”
    2. At each element, I decide whether to:
       ---start a new subarray from the current element, or
       ---extend the previous subarray.”
    3. Recursion:  I take the max between the cur element itselt and the cur element plus the prev sum..
    4. I also track the global maximum that stores the best subarray seen so far.
    """
    cur_sum = num[0]
    max_sum = num[0]

    for i in range(1, len(num)):
        cur_sum = max(num[i], cur_sum + num[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(
    f'Maximum SubArry of {[-1, 2, 3, 6, -5]} is {maxSum1([-1, 2, 3, 6, -5])}')

print("=========== Return the SubArray too....!")
""" “So this gives me the maximum subarray sum in O(n) time and O(1) space.
If needed, I can extend this to also return the actual subarray by tracking indices.


===Idea: “To do that, I’ll keep track of where the current subarray starts,
           and whenever I find a new maximum, I’ll record its start and end positions.
           
           1. temp_start, best_start and best_end”"""


def maxSumArrayPartB(num):
    # Return the max and the subarrays itself
    cur_sum = num[0]
    max_sum = num[0]

    # three variables
    temp_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(num)):
        # cur_sum = max(num[i], cur_sum + num[i])

        """Part A — Decide Restart vs Continue"""

        # 1.  I compare num[i] and cur_sum + num[i].
        # 2. If num[i] is larger, I restart the subarray at index i and update temp_start.
        # 3. Otherwise, I continue the existing subarray
        if num[i] > cur_sum + num[i]:
            cur_sum = num[i]
            temp_start = i
        else:
            cur_sum += num[i]

        # max_sum =  max(cur_sum, max_sum)
        """Part B — Update Global Best"""

        # 1. After updating the current sum, I check if it’s greater than the global maximum.
        # 2. If it is , I update max_sum and store the current subarray boundaries using temp_start and the current index.
        if cur_sum > max_sum:
            max_sum = cur_sum
            best_start = temp_start
            best_end = i

    return max_sum, num[best_start: best_end + 1]


print(
    f'Maximum SubArry of {[-1, 2, 3, 6, -5]} and Return array is {maxSumArrayPartB([-1, 2, 3, 6, -5])}')
