class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqCounter = {}
        for i in range(len(s)):
            freqCounter[s[i]] = freqCounter.get(s[i],0) + 1
            freqCounter[t[i]] = freqCounter.get(t[i],0) - 1

        for n in freqCounter.values():
            if n != 0:
                return False

        return True            


        