class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies 
        # add to heap of size k
        # return heap
        
        freqCount = Counter(nums)
        minHeap = []

        for num,freq in freqCount.items():
            heapq.heappush(minHeap, (freq,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for freq,num in minHeap]   