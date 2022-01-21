'''' Solution uses reverse funtion to reavers each words and they are then joined in the string 
using join method'''

class Solution:
    
    def rev(self, s:str) -> str:
        s = s[::-1]
        return s
    
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        
        for i in range(len(ls)):
            ls[i] = self.rev(ls[i])
        
        s = " ".join(ls)
        
        return s