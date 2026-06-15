class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for num,freq in freqMap.items():
            buckets[freq].append(num)

        # try to retrive k elements from it by traversing in reverse order
        res = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res




        