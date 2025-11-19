class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charMap = {}
        maxLength = 0

        maxFreq = 0

        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r],0) 
            maxFreq = max(maxFreq,charMap[s[r]])

            #check if window is valid
            #while (r-l+1) - max(charMap.values()) > k:
            while (r-l+1) - maxFreq > k:
    
                charMap[s[l]] -= 1 
                l += 1

            maxLength = max(maxLength, r-l+1)    

        return maxLength    
        