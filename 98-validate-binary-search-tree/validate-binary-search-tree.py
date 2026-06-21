# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, low, high):
            # An empty tree/leaf child is always a valid BST
            if not node:
                return True
            
            # The current node's value MUST strictly be within the allowed range
            if not (low < node.val < high):
                return False
            
            # Recurse left (update high boundary) and right (update low boundary)
            return check(node.left, low, node.val) and check(node.right, node.val, high)
        
        # Start with the ultimate boundaries: negative and positive infinity
        return check(root, float('-inf'), float('inf'))