class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)

        baba = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }

        count = 0
        while True:
            if (d['b'] >= 1 and
                d['a'] >= 1 and
                d['l'] >= 2 and
                d['o'] >= 2 and
                d['n'] >= 1):

                d['b'] -= 1
                d['a'] -= 1
                d['l'] -= 2
                d['o'] -= 2
                d['n'] -= 1
                count += 1
            else:
                return count
                