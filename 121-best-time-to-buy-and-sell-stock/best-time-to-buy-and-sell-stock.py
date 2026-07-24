class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                p = prices[r] - prices[l]
                r += 1
                max_profit = max(max_profit, p)
        return max_profit
