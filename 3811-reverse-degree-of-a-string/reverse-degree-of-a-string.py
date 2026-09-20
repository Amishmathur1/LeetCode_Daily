class Solution:
    def reverseDegree(self, s: str) -> int:
        # print(123 - ord('a'), 123 - ord('z'))
        ans = 0
        for i in range(len(s)):
            ans += (123 - ord(s[i])) * (i+1)
        return ans