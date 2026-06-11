class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        minheap = []

        for num,freq in freqMap.items():
            heapq.heappush(minheap,(freq,num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        return [num for freq,num in minheap]                