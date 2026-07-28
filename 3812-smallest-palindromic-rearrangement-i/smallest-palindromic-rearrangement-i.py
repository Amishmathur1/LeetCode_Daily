class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = [''] * len(s)
        d = Counter(s)

        ind = 0
        while ind < len(s)//2:
            for ch in sorted(d):
                if d[ch] >= 2:
                    l[ind] = ch
                    l[-(ind+1)] = ch
                    d[ch] -= 2
                    if d[ch] == 0:
                        del d[ch]
                    break
            ind += 1

        if len(s) % 2:
            for ch in d:
                if d[ch] == 1:
                    l[len(s)//2] = ch
                    break

        return (''.join(l))