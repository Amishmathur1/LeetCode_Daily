class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tot = 0

        for i in range(len(tickets)):

            if i <= k:
                tot += min(tickets[i], tickets[k])

            else:
                tot += min(tickets[i], tickets[k] - 1)

        return tot