class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        max_seq = 1
        curr_seq = 1

        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                curr_seq += 1
                max_seq = max(max_seq, curr_seq)
            
            elif nums[i] == nums[i + 1]:
                continue

            else:
                curr_seq = 1
        return max_seq
