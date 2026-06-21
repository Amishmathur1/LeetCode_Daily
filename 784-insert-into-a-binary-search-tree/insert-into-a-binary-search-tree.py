# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)

        def dfs(root):
            nonlocal newNode
            if root is None:
                return newNode
            
            if root.val < val:
                root.right =  dfs(root.right)
            if root.val >= val:
                root.left =  dfs(root.left)
            
            return root
        
        return dfs(root)

