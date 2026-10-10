import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        heap = []
        res = []

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for value, count in freq.items():
            heapq.heappush(heap, (count, value))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
