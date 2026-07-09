class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
            

        return "".join(f"{(len(s))}#{s}" for s in strs)    
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i, j = 0, 0
        res = []
        while i < len(s):
            j = i + 1
            while(s[j] != '#'):
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + 1 + length

        return res    

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))