import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for dist, x, y in heap]