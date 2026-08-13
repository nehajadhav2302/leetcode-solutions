class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
        
    def maxPairStrength(self, nums: list[int]) -> int:
        max_strength = float('-inf')

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                g = self.gcd(nums[i], nums[j])
                strength = (nums[i] // g) * (nums[j] // g)
                max_strength = max(max_strength, strength)
        return max_strength
