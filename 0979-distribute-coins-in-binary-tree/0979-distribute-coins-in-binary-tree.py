# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(curr):
            if not curr:
                return 0
            nonlocal res
            
            l = dfs(curr.left)
            r = dfs(curr.right)

            c = 1 - curr.val + l + r
            res += abs(c)
            return c
        dfs(root)
        return res

            