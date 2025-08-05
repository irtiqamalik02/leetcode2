class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key : searchiuig ofr , val will be index
        twoSumHash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in twoSumHash:
                return [i,twoSumHash[complement]]
            twoSumHash[nums[i]] = i
            
        #return [-1,-1]    