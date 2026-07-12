# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        d = defaultdict(list)
        ans = []

        def dfs(root, row=0, col=0):
            if not root:
                return

            d[col].append((row, root.val))

            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
            return d
        d = dfs(root)
        # print(d)
        for col in sorted(d):
            d[col].sort()          
            ans.append([val for row, val in d[col]])
        return ans