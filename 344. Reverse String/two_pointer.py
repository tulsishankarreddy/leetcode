''' Solution using two pointer method'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while (left < right):  #We can also use condition (left < (len(s)//2))
            s[left], s[right] = s[right], s[left] #swapping the values
            left +=1
            right -=1