class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for n in range(len(nums)):
            complement = target - nums[n]
            if complement in hashmap:
                return [n,hashmap[complement]]  
            hashmap[nums[n]] = n