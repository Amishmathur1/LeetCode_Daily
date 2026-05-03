class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res = ""
        
        for i in range(len(s)):
            # Case 1: Odd length (center is s[i])
            tmp = self.expand(s, i, i)
            if len(tmp) > len(res):
                res = tmp
                
            # Case 2: Even length (center is between s[i] and s[i+1])
            tmp = self.expand(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
                
        return res

    def expand(self, s, left, right):
        # Expand outwards as long as it's a palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the substring found
        return s[left + 1:right]