class Solution:
    def calHour(self, piles, h):
        hour = 0
        for pile in piles:
            hour += math.ceil(pile / h)
        return hour

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        maxpile = max(piles)
        low = 1
        high = maxpile
        ans = maxpile

        while low <= high:
            mid = (low + high) // 2
            totalH = self.calHour(piles, mid)

            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans