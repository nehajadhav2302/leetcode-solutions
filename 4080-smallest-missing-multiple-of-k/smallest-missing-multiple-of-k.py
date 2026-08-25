class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        ans = k
        
        while ans in nums_set:
            ans += k
        return ans