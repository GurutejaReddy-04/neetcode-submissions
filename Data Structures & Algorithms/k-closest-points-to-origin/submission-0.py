class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            max_heap = []

            for x, y in points:
                distance = x * x + y * y

                heapq.heappush(max_heap, (-distance, [x, y]))

                # Keep heap size fixed at k
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

            result = []

            for distance, point in max_heap:
                result.append(point)

            return result
        