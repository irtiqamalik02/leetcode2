class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            #skip dupes for first value
            if i > 0 and  nums[i-1] == nums[i]:
                continue

            # two sum approach
            l,r = i+1, len(nums) - 1   
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r] 

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #update pointers
                    l += 1
                    r -= 1   

                    # skip dupes
                    while l < r and nums[l] == nums[l-1]: # since already updated
                        l += 1     
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

            
        return res            
        