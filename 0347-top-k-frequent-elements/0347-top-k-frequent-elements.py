class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter
        freqCounter = Counter(nums)
        # heap freq,num
        minHeap = []
        for num,freq in freqCounter.items():
            heapq.heappush(minHeap,(freq,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for freq,num in minHeap]        

        