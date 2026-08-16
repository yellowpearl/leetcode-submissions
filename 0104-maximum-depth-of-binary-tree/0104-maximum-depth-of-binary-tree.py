# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr) -> int:
            if not curr:
                return 0
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            return 1 + max(l, r)
        return dfs(root)
        