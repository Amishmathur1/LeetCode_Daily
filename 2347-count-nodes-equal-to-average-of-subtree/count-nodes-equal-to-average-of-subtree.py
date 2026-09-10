# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = []
        count = 0
        def findAvg(root):
            nonlocal count
            if not root:
                return 

            avg = bfs(root)
            if avg == root.val:
                count += 1

            if root.left:
                findAvg(root.left)
            if root.right:
                findAvg(root.right)

            return count 

        def bfs(root):
            dq = deque([root])
            tot_sum = 0
            tot_ele = 0

            while dq:
                root = dq.popleft()
                tot_ele += 1
                tot_sum += root.val

                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)

            avg = tot_sum//tot_ele
            return avg

        return findAvg(root)