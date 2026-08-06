class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            num = str(n)
            check = 1
            for i in num:
                check *= int(i)
            
            if check % t == 0:
                return int(num)
            
            n += 1