class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = []
        odd = []
        i = 1
        while len(even) < n:
            if i % 2 != 0:
                odd.append(i)
            else:
                even.append(i)
            i += 1

        a = sum(even)
        b = sum(odd)
        print(a, b)
        return gcd(a,b)