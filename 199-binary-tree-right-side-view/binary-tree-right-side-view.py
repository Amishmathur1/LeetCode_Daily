# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:    return []

        dq = deque([root])
        lmao = []
        
        while dq:
            size = len(dq)
            haha = []
            for _ in range(size):
                node = dq.popleft()
                haha.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            lmao.append(haha[-1])
        return lmao