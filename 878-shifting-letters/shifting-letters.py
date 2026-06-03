class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        dummy = 'abcdefghijklmnopqrstuvwxyz'
        # print(len(dummy))
        x = ''
        tot_sum = sum(shifts)

        for i in range(len(s)):
            a = (dummy.index(s[i]) + tot_sum) % len(dummy)
            tot_sum -= shifts[i]
            x += dummy[a]
        return x
