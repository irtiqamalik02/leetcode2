class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for n in nums:
            if n in uniques:
                return True
            uniques.add(n)

        return False    

        