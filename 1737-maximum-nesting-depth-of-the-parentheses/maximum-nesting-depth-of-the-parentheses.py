class Solution:
    def maxDepth(self, s: str) -> int:
        max_d = 0
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                max_d = max(max_d, cnt)
                cnt -= 1
        
        return max_d