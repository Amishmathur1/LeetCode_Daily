class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        x = sorted(costs)
        ans = coins
        count = 0
        print(x)
        for i in x:
            ans -= i
            if ans >= 0:
                print(ans)
                count += 1
        return (count) 