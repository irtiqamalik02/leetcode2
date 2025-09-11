class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq
        freqMap = Counter(nums)
        # add to heap
        minHeap = []
        for num,freq in freqMap.items():
            heapq.heappush(minHeap, (freq,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)       

        # return k elements from heap
        return [num for freq,num in minHeap]

        