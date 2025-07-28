class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = {}

        for n in s:
            charCount[n] = charCount.get(n,0)+1
        
        for n in t:
            charCount[n] = charCount.get(n,0)-1

        for val in charCount.values():
            if val != 0:
                return False    

        return True          
        

     # sort and compare n log n   