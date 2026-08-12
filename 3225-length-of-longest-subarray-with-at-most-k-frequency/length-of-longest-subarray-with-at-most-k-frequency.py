class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            # Shrink window from the left if current element exceeds frequency k
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Max window size is the current valid subarray length
            max_len = max(max_len, right - left + 1)
            
        return max_len