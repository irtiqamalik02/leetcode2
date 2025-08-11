class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = [1] 
        postFix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            preFix.append(preFix[-1] * nums[i])  
        preFix = preFix[0:len(preFix)-1]

          
        
        for i in range(len(nums) - 1, -1, -1):
            postFix[i] = postFix[i + 1] * nums[i]

        postFix = postFix[1:len(postFix)+1]  
 

        res = []
        for n1,n2 in zip(preFix,postFix):
            res.append(n1*n2)

        return res    


        