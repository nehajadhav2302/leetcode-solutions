class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result =[1] * n
        prefix = [1] * n
        sufix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            sufix[j] = sufix[j + 1] * nums[j + 1]

        for i in range(n):
            result[i] = prefix[i] * sufix[i]
        return result