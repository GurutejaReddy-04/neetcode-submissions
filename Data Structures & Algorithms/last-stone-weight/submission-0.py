class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, -1*i)

        while len(heap) >=2:
            a = -1*heapq.heappop(heap)
            b = -1*heapq.heappop(heap)

            if a!=b:
                heapq.heappush(heap, -1* abs(a-b))

        if heap:
            return -1*heap[0]
        else:
            return 0


            
            

            
        