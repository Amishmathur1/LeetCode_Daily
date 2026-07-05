class Solution:
    def countPrimes(self, n: int):
        if n < 2:
            return 0

        a = [0 for i in range(n)]
        a[0] = 1
        a[1] = 1

        for i in range(2, n):
            for j in range(i + i, n, i):
                a[j] = 1

        count = 0

        for i in range(n):
            if a[i] == 0:
                count += 1

        return count