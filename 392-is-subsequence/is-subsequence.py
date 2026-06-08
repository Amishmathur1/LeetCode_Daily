class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        for i in range(len(t)):
            if a == len(s):
                break
            if s[a] == t[i]:
                a += 1
        if a == len(s):
            return True
        else:
            return False