class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Only start counting if n is the start of a sequence
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
            


      # sequence start -> no left neighbor

        # identify sequence starts and try to form lists
        # keep note of longest list

        # put in set
                 

        