class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        values = set(nums)

        reachable2 = [False]*2048
        reachable3 = [False]*2048


        for first in values:
            for second in values:
                reachable2[first^second] = True


        for xor in range(2048):
            if reachable2[xor]:
                for c in values:
                    reachable3[xor^c] = True

        return sum(reachable3)