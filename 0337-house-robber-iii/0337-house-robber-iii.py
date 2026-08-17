# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr):
            if not curr:
                return 0, 0
            
            l1, l2 = dfs(curr.left)
            r1, r2 = dfs(curr.right)

            c1 = curr.val + l2 + r2
            c2 = max(l1, l2) + max(r1, r2)
            return c1, c2
        
        c1, c2 = dfs(root)
        return max(c1, c2)
