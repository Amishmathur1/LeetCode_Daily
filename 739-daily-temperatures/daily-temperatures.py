class Solution:
    def dailyTemperatures(self, x: List[int]) -> List[int]:

        n = len(x)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and x[i] > x[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans
