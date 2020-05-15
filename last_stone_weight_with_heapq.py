import heapq

def lastStoneWeight(stones) -> int:
    heapq.heapify(stones)
    heap = []
    for i in stones:
        heapq.heappush(heap, -1 * i)

    while len(heap) > 1:
        diff = (-1 * heapq.heappop(heap)) - (-1 * heapq.heappop(heap))
        if diff:
            heapq.heappush(heap, diff)

    return heap[0] if heap else 0

# For testing
st = [2,7,4,1,8,1]


print(lastStoneWeight(st))
