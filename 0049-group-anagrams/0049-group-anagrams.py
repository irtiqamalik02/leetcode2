class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqCount = {}

        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1

            freqCount.setdefault(tuple(charCount),[]).append(s)

        return list(freqCount.values())    
        