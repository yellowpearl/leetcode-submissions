# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # через preorder можно получить корень, все что в inorder находится до корня будет левее, остальное правее
        # 10 минут пришел к решению, O(n) - каждую ноду обойти O(h) - высота дерева по памяти
        
        def dfs(preorder, inorder):
            if not preorder:
                return None

            node_val = preorder[0]
            node = TreeNode(preorder[0])


            i = inorder.index(node_val)
            
            left_ino = inorder[:i]
            left_ino_s = set(left_ino)
            left_pre = [n for n in preorder if n in left_ino_s]

            node.left = dfs(left_pre, left_ino)

            right_ino = inorder[i+1:]
            right_ino_s = set(right_ino)
            right_pre = [n for n in preorder if n in right_ino_s]

            node.right = dfs(right_pre, right_ino)

            return node

        return dfs(preorder, inorder)


        
        