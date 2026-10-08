class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        values = set(nums)
        max_seq = 0

        for value in values:
            if value - 1 in values:
                continue
            
            curr_seq = 1
            next_value = value + 1

            while next_value in values:
                curr_seq += 1
                next_value += 1
            max_seq = max(max_seq, curr_seq)
        return max_seq