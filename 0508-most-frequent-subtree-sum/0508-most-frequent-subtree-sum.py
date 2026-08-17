# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        
        def dfs(curr) -> int:
            if not curr:
                return 0
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            s = curr.val + l + r
            count[s] += 1
            return s
        dfs(root)
        m = max(list(count.values()))
        return [k for k, v in count.items() if v == m]