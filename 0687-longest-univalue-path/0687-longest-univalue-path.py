# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr) -> tuple[int, int | None]:
            if not curr:
                return 0, None
            nonlocal res

            l_c, l_v = dfs(curr.left)
            r_c, r_v = dfs(curr.right)

            c_c = 1
            c_v = curr.val
            
            if c_v == l_v == r_v:
                res = max(res, l_c+r_c)
                c_c += max(l_c, r_c)
            elif c_v == l_v:
                res = max(res, l_c)
                c_c += l_c
            elif c_v == r_v:
                res = max(res, r_c)
                c_c += r_c
            
            return c_c, c_v
        dfs(root)
        return res
                