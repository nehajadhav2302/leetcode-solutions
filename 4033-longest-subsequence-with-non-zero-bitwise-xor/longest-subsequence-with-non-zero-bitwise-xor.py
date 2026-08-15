class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total ^= num
        
        if total != 0:
            return len(nums)
        
        for num in nums:
            if num != 0:
                return len(nums) - 1
        return 0