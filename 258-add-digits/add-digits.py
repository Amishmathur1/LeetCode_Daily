class Solution:
    def addDigits(self, num: int) -> int:
        new_sum = num
        while new_sum > 9:
            y = 0
            x = str(new_sum)
            for i in x:
                y += int(i)
            new_sum = y
        return new_sum