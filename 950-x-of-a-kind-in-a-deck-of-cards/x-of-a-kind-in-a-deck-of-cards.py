from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        d = Counter(deck)
        x = list(d.values())

        for size in range(2, min(x) + 1):

            valid = True

            for freq in x:
                if freq % size != 0:
                    valid = False
                    break

            if valid:
                return True

        return False