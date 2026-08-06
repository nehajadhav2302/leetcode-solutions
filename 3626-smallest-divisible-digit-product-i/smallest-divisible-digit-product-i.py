class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n <= 100:
            num = n
            prod = 1

            while num > 0:
                prod *= num % 10
                num //= 10
            if prod % t == 0:
                return n
            n += 1