class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
        
        d = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def dfs(ind, path):
            if ind == len(digits):
                ans.append(''.join(path))
                return
            
            for ch in d[digits[ind]]:
                path.append(ch)
                dfs(ind + 1, path)
                path.pop()
        dfs(0, [])
        if ans == ['']: return []
        return ans        