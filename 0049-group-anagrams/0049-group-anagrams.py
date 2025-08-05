class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for s in strs:
            key = tuple(sorted(s))
            anagramMap.setdefault(key,[]).append(s)

        result = []
        for val in anagramMap.values():
            result.append(val)

        return result    




        