# # ================== Path Sum =====================
# # Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf
# # path such that adding up the values along the path equals targetSum.

# class Solution:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     def hasPathSum(self, root, targetSum: int):

#         # DFS function
#         def has_sum(root, cur_sum):
#             if not root:
#                 return False

#             cur_sum += root.val

#             if not root.left and not root.right:
#                 return cur_sum == targetSum

#             return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
#         has_sum(root, 0)

#     # Inverted Binary Tree Leeetcode 226
#     def invertTree(self, root):
#         if not root:
#             return None
#         root.left, root.right = root.right, root.left

#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root

#         # time: O(n)-- space: O(h) where h is height of the tree.


#         # input: = [4,2,7,1,3,6,9]
#         # output: [4, 7, 2, 9, 6, 3, 1]
#         # Key ideas: switch root.l and root.r , then,----do it recursively...
# input1 = [4, 2, 7, 1, 3, 6, 9]
# sol = Solution()
# res = sol.invertTree(input1)
# print(f'Inverted Tree of {input1} is =  {res}')


from collections import deque
from typing import Optional, List

# Basic binary tree node


class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS helper: check if any root-to-leaf path sums to target
        def dfs(node: Optional[TreeNode], cur_sum: int) -> bool:
            if not node:
                return False
            cur_sum += node.val
            # If leaf: verify accumulated sum
            if not node.left and not node.right:
                return cur_sum == targetSum
            # Recurse down either side
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)  # <-- important: return the result

    # LeetCode 226 – Invert Binary Tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Swap children
        root.left, root.right = root.right, root.left
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root  # time: O(n), space: O(h) (h = height)
    # =============== max depth problem =======

    def maxDepth(self, root):
        if not root:
            return None

        # recursice left and right
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


# ------- Helpers for testing (level-order with None for missing nodes) -------


def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order list (use None for missing)."""
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for v_left, v_right in zip(it, it):
        node = q.popleft()
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)
        if v_right is not None:
            node.right = TreeNode(v_right)
            q.append(node.right)
    return root


def to_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize tree to level-order list (trim trailing None)."""
    if not root:
        return []
    q = deque([root])
    out: List[Optional[int]] = []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # remove trailing None for pretty output
    while out and out[-1] is None:
        out.pop()
    return out


# ----------------------- Quick tests -----------------------
# Example tree: [4,2,7,1,3,6,9]
arr = [4, 2, 7, 1, 3, 6, 9]
root = build_tree(arr)

sol = Solution()

# Test invertTree
inv_root = sol.invertTree(root)
print("Inverted:", to_level_order(inv_root))  # expected: [4,7,2,9,6,3,1]

# Test hasPathSum (e.g., path 4->7->6 = 17; 4->7->9 = 20; 4->2->1 = 7; etc.)
print("Has path sum 20?:", sol.hasPathSum(inv_root, 20))  # True (4->7->9)
print("Has path sum 26?:", sol.hasPathSum(inv_root, 26))  # False
