from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        # store indices of every character
        pos = defaultdict(list)

        for i, ch in enumerate(s):
            pos[ch].append(i)

        ans = 0

        for word in words:

            prev = -1
            found = True

            for ch in word:

                # if character not present at all
                if ch not in pos:
                    found = False
                    break

                arr = pos[ch]

                # find first index > prev
                idx = bisect_right(arr, prev)

                # no valid next index
                if idx == len(arr):
                    found = False
                    break

                # update prev
                prev = arr[idx]

            if found:
                ans += 1

        return ans