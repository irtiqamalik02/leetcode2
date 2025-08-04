class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charFreqMap = {}

        for i in range(len(s)):
            charFreqMap[s[i]] =  charFreqMap.get(s[i],0)+1
            charFreqMap[t[i]] =  charFreqMap.get(t[i],0)-1

        for val in charFreqMap.values():
            if val != 0:
                return False

        return True            