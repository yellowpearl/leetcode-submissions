# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            res = max(res, l+r)
            return max(l, r) + 1
        dfs(root)
        return res
        