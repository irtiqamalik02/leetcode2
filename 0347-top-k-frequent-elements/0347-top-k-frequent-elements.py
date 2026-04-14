class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter freq
        freqMap = Counter(nums)

        # initailise list of buckets
        buckets = [[] for i in range(len(nums)+1)]

        # add to bucket based on freq
        for num,freq in freqMap.items():
            buckets[freq].append(num)

        # traverse in reverse
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        