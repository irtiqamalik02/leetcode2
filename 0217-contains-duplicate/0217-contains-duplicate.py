class Solution:
    def containsDuplicate(self, nums):
        uniques = set(nums)
        return len(nums) != len(uniques)