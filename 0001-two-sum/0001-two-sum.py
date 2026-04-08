class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in hashMap:
                return [i,hashMap[complement]]

            hashMap[n] = i



        