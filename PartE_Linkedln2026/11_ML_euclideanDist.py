""" Euclidean Distance - Practical Machine Learning Tutorial with Python p.15
--- Used mostly for KNN-algorithmss...!


Next time==== STEPS=====:

1. “Compute distances”
2. “Sort indices using argsort”
3. “Select top k”
4. “Use Counter for majority vote”

 """


import numpy as np
from collections import Counter


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
    k_labels = [y[i] for i in k_ind]
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
