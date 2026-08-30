class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        L = min(min_idx, max_idx)
        R = max(min_idx, max_idx)

        option1 = R + 1
        option2 = n - L
        option3 = (L + 1) + (n - R)

        return min(option1, option2, option3)