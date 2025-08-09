class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]

        # count Frequencies
        freqMap = Counter(nums)

        # add to buckets based on freqs
        for num,freq in freqMap.items():
            buckets[freq].append(num)

        res = []
        # traverse in reverse 
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


