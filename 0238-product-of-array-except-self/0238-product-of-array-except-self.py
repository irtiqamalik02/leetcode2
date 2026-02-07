class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix.append(prefix[-1] * nums[i])

        prefix = prefix[0:len(nums)]

        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        postfix = postfix[1:len(postfix)+1]   

        res = []
        for n1,n2 in zip(prefix,postfix):
            res.append(n1*n2) 

        return res    
            
        