class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate, sort , insert to hashmap

        hashMap = {}
        for s in strs:
            hashMap.setdefault(tuple(sorted(s)),[]).append(s)

        return list(hashMap.values())    
