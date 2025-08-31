# =========== Union and Interception of two Arrays ==============

arr1 = [2,3,4,5]
arr2 = [1,7,9,3,1,4,8]

def unionIntersection(arr1, arr2):
    return "Union = ", list(set(arr1) | set(arr2)) , "Intersection = ", list(set(arr1) & set(arr2))

print(unionIntersection(arr1, arr2))

def intersection_two_pointer(arr1, arr2):
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    return result

print(intersection_two_pointer(arr1, arr2))
      
      