class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies
        freqCount = Counter(nums)

        # create buckets cappped at size of arr
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # using freq as index put items in buckets
        for num,freq in freqCount.items():
           buckets[freq].append(num)
        # traverse in reverse and return top k frequenct elements

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


        