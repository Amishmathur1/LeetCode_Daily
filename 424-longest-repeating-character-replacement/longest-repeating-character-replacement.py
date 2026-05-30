class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        l = 0
        ans = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            while ((r - l + 1) - max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return (ans)