""" ========= Trapping Rain Water - Leetcode 42 - 2 Pointers (Python)

Q1: Given n non-negative integers rerpresenting an elevation map where the width of each bar is 1, compute 
how much water it can trap after raining...!
"""


def trapping_water(height):
    n = len(height)
    left, right = 0, n - 1  # both pointers
    left_max = 0
    right_max = 0
    trapping_water = 0

    # using pointer
    while left < right:
        if height[left] < height[right]:
            # if current bar is shorter than left bar we can trap water
            if height[left] < left_max:
                trapping_water += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            # checking for right side
            if height[right] < right_max:
                trapping_water += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    return trapping_water


input1 = [4, 2, 0, 3, 2, 5]
# output = 9
print(f'Totol water trapped in {input1} is {trapping_water(input1)} ')

input2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
