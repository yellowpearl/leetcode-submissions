# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(curr, compare_to):
            if not curr:
                return [None]
            nonlocal res
            ret = [curr.val]
            l = dfs(curr.left, compare_to)
            r = dfs(curr.right, compare_to)
            ret.extend(l)
            ret.extend(r)
            if ret == compare_to:
                res = True
            return ret
        comp = dfs(subRoot, [None])
        dfs(root, comp)
        return res
