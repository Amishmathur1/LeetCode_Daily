class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if len(str(num1)) == 2 and len(str(num2)) == 2:
            return 0
        
        count = 0

        for i in range(num1, num2+1):
            x = str(i)
            if len(x) > 2:
                for j in range(1, len(x)-1):
                    # Checking for Peaks
                    if x[j-1] > x[j] and x[j] < x[j+1]:
                        count += 1
                    
                    elif x[j-1] < x[j] and x[j] > x[j+1]:
                        count += 1
        return count
