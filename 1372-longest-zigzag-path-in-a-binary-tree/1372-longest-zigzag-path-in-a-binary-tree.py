# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(curr):
            if not curr:
                return 0, 0
            nonlocal res
            _, lr = dfs(curr.left)
            rl, _ = dfs(curr.right)

            cl = rl + 1
            cr = lr + 1

            res = max(res, cl, cr)
            return cr, cl
        dfs(root)
        return res - 1


        