# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0

        def dfs(root):           
            nonlocal count
            if not root:
                return float('-inf')
            
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            ans = max(root.val, max_left, max_right)
            if root.val == ans:
                count += 1
            
            return ans 

        dfs(root)
        return count