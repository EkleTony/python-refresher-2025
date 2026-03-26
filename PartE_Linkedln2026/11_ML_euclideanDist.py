""" Euclidean Distance - Practical Machine Learning Tutorial with Python p.15
--- Used mostly for KNN-algorithmss...!


Next time==== STEPS=====:

1. “Compute distances”
2. “Sort indices using argsort”
3. “Select top k”
4. “Use Counter for majority vote”




===============From LInkedln coding=============
my soln after he helping me alot def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


Q1: Basic KNN Implementation
Problem Statement
Implement a K-nearest neighbors classifier using Euclidean distance.


Input:
import numpy as np
X = [
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [5.0, 6.0],
    [6.0, 7.0]
]
y = [0, 0, 1, 1, 1]
test_point = [4.0, 5.0] 
k = 3
Starter Code:
from collections import Counter
class KNNClassifier:
    def __init__(self, X: List[List[float]], y: List[int], k: int):
        pass
    def euc_distance(a, b):
        # sqrt ( sum of (x2-x1)^2)
        euc_dist = np.sqrt(np.sum((a-b)**2 ))
        return euc_dist

    def predict(self, test_point: List[float]) -> int:
        distance = [euc_distance(x, test_point ) for x in X]

        # k-smallest distance
        k_ind = np.argsort(distance)[:k]

        #majority vote
        top_common = Counter([y[i] for i in k_ind])
        top_common.most_common
        






## sqrt_root( (y-x)

## x_new = 4 y_new = have to predict this
## 
X = [
    [1.0],
    [2.0],
    [3.0],
    [5.0],
    [6.0]
]
y = [0, 0, 1, 1, 1]
##
## predict y for a new x. would get the K nearest neighbors to x. 

## loop thru all of x, for each x index (find the Euclidean distance
# btw (X - x_new))
# say k=2
# k_indices = sort all distance with k most top elments
# loop thru my k_indices and get majority vote y[i] where i is from k_indeces and get the most common(1)-- topk
#



Clean pseudocode (interview-ready)

“
1. First, I loop through all training points and compute the Euclidean distance to the query point.
2. Then, I store all distances and sort them.
3. Next, I select the indices of the k smallest distances.
4. Using those indices, I retrieve the corresponding labels.
Finally, I return the most common label among those neighbors.”
 """

# 1. euclidean distance -- to the query point.
# sqrt ( sum_i^n( (a-b)**2 ) )

import numpy as np
from collections import Counter


import numpy as np
from collections import Counter


def euclidean_distance(a, b):
    return np.sqrt(np.sum((np.array(a) - np.array(b)) ** 2))


def manhattan_distance(a, b):
    return np.sum(np.abs(np.array(a) - np.array(b)))


def predict(X, y, test_point, k=3):
    distances = [euclidean_distance(x, test_point) for x in X]
    k_indices = np.argsort(distances)[:k]
    x_points = [X[i] for i in k_indices]
    k_labels = [y[i] for i in k_indices]
    # majority vote
    prediction = Counter(k_labels).most_common(2)[0][0]

    # new print
    print(f"Test Points: {test_point}")
    print(f'nearest {k} points: {x_points}')
    print(f'their labels: {k_labels}')
    print(f'Predicted label: {prediction}')

    print("==================================================")

    return prediction


X1 = [[2.4, 5.0], [1.0, 3.0], [1.4, 5.0], [7.0, 3.0]]
y1 = [0, 1, 1, 0]
test_x1 = [1.5, 2.4]

distances = [euclidean_distance(x, test_x1) for x in X1]
print("==================================================")

print("All X points:", X1)
print("Prediction:", predict(X1, y1, test_x1, k=2))
print()


def euclidean_distance(p1, p2):
    # Sum of n(i-to-n)--,
    # euc_dist = np.sqrt( --> Sum_i^n  --> (p1-p2)**2))
    eud_dist = np.sqrt(np.sum((np.array(p1) - np.array(p2))**2))

    return eud_dist


def predict(X, y, test_point):
    k = 3
    distance = [euclidean_distance(x, test_point) for x in X]

    # return distance
    # === Get k-indices for majority votes
    k_ind = np.argsort(distance)[:k]
    # k_indices = [2, 3, 1], y = [0, 0, 1, 1, 1]
    k_labels = [y[i] for i in k_ind]
    # [1, 1, 0]
    return Counter(k_labels).most_common(1)[0][0]


X = [
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [5.0, 6.0],
    [6.0, 7.0]
]
y = [0, 0, 1, 1, 1]
test_point = [4.0, 5.0]

print(f'Euclidean distance of {X} =  {predict(X, y, test_point)}')
