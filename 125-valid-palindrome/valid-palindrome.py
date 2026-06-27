class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        for i in s:
            if i.isalnum():
                x += i.lower()
        
        print(x)

        def check(l, r):
            if l >= r:
                return True
            if x[l] != x[r]:
                return False
            
            return check(l+1, r-1)
        return check(0, len(x)-1)