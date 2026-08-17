# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr, min_val, max_val):
            if not curr:
                return 
            nonlocal res
            res = max(res, abs(curr.val-min_val), abs(curr.val-max_val))
            min_val = min(min_val, curr.val)
            max_val = max(max_val, curr.val)
            dfs(curr.left, min_val, max_val)
            dfs(curr.right, min_val, max_val)
        
        dfs(root, root.val, root.val)
        return res
        