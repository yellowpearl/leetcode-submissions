# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            
            l = max(dfs(curr.left), 0)
            r = max(dfs(curr.right), 0)
            res = max(res, l+r+curr.val)
            return curr.val + max(l, r)
        
        dfs(root)
        return res
        