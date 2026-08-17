# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return [None]
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            ret = [curr.val]
            ret.extend(l)
            ret.extend(r)
            return ret
        
        p_rep = dfs(p)
        q_rep = dfs(q)
        return p_rep == q_rep