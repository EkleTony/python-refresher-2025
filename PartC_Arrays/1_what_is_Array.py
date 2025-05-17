# ================== What is ARRay? ======================

"""_summary_ Arrays ============ Static vs Dynamic Arrays =================

    1. Static Array: get allocated memory at compile and its size is fixed

    2. Dynamic Arrays: get automatially grows when we try to make insertion and there is no space left for new items

    """
def leaderArray(arr):
    maxArr = arr[0]
    lst = []
    
    for val in arr:
        if maxArr < val:
            lst.append(val)
    return lst

x = leaderArray([34,5,6,77,8,22,1])
print(x)
             