class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        l, r = 0, 0
        d = defaultdict(int)
        count = 0

        while l <= len(s) - 3:
            if r >= len(s):
                l += 1
                r = l
                d = defaultdict(int)
            d[s[r]] += 1            
            
            while d['a'] >= 1 and d['b'] >= 1 and d['c'] >= 1:
                count += len(s) - r

                d[s[l]] -= 1
                l += 1
            else:
                r += 1
        return count 
            

        

