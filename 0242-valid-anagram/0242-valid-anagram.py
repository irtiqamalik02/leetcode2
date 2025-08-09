class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # count the frequency of characters in both strings and comapre the hashmaps

        charFreq = {}       
        
        for i in range(len(s)):
            charFreq[s[i]] = charFreq.get(s[i],0) + 1
            charFreq[t[i]] = charFreq.get(t[i],0) - 1

        for val in charFreq.values():
            if val != 0 :
                return False

        return True            