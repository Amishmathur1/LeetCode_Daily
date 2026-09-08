import sys
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        sys.set_int_max_str_digits(0)
        l = []

        t = 0

        for i in word:
            t = (t * 10 + int(i)) % m
            l.append(1 if t == 0 else 0)
        
        return l