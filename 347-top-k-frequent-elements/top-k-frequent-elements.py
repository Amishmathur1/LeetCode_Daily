class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        #print(d)

        ans = sorted(d, key=d.get, reverse=True)[:k]
        return ans