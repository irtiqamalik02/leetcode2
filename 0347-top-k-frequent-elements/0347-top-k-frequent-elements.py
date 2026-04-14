class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]

        freqMap = Counter(nums)
        # add to bucket based on freq
        for n,f in freqMap.items():
            bucket[f].append(n)

        res = []
        # traverse in reverse and fetch k elements
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res



                


        