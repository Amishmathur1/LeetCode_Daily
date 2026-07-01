class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        path = []
        ans = []

        def backtrack(o, c):

            if o == c == n:
                ans.append(''.join(path))
                return 
            
            if o > c:
                path.append(')')
                backtrack(o, c+1)
                path.pop()
            
            if o < n:
                path.append('(')
                backtrack(o+1, c)
                path.pop()
        
        backtrack(0, 0)
        return ans