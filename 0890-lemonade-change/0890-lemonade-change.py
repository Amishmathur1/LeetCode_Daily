from collections import Counter
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = Counter(bills)
        if d[10] > d[5]:
            return (False)
        if d[10] == d[5] and d[20] > 0:
            return (False)

        x = {5:0,10:0,20:0}
        for i in bills:
            if i == 5:
                x[5] += 1
            if i == 10:
                if x[5] > 0:
                    x[5] -= 1
                    x[10] += 1
                else:
                    return (False)
            if i == 20:
                if x[10] > 0 and x[5] > 0:
                    x[10] -= 1
                    x[5] -= 1
                    x[20] += 1
                elif x[5] > 2:
                    x[5] -= 3
                    x[20] += 1
                else:
                    return (False)
        return True