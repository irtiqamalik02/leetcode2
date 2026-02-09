class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # identify start of sequence
        # get the length of sequence
        longest = 0
        numset = set(nums)

        for n in numset:
            if n-1 not in numset:
                length = 1
                while n+length in numset:
                    length += 1
                
                longest = max(longest,length)

        return longest        

        