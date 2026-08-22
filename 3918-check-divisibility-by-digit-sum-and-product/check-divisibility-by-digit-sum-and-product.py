class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        total = 0
        prod = 1
        while n > 0:
            rem = n % 10
            n //= 10
            total += rem
            prod *= rem
        
        if temp % (total + prod) == 0:
            return True
        return False