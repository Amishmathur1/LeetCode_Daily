class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''

        #normallizing the string
        for i in s:
            if i.isalpha() or i.isdigit():
                i = i.lower()
                x += i
            else:
                continue

        #using 2 pointers for palindrome checking
        l, r = 0, len(x)-1

        while l < r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
                
        return True
