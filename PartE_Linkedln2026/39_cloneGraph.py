""" =======Clone Graph - Leetcode 133 - Graphs (Python)


***Problem idea

--You are given a reference to a node in a connected undirected graph.
--You need to return a deep copy of the whole graph.

Note: ===== That means:=====
--new nodes
--same values
--same neighbor connections
--no reuse of original nodes
e.g

(1)-----(2)                (1)        (2)
|        |   ---------->   
|        |  dfs to create    
(3)-----(4)                 (3)        (4)

steps:
--dfs
--hashmap for references  {(3): (3), (1): (1), ....}
--
"""
