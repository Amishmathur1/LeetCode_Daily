class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        x = ''
        for i in str(n):
            if i != '0':
                x += i
        
        summ = 0
        for i in x:
            summ += int(i)

        return int(x) * summ