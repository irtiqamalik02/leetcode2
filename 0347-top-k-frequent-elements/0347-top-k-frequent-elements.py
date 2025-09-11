class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq
        freqMap = Counter(nums)

        # add to bucket based on freq
        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in freqMap.items():
            buckets[freq].append(num)

        # traverse in reverse
        res = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
            if len(res) == k:
                return res   


        