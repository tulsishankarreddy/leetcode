''' Solution avoiding sorting the list'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        #We can use 2 pointer method to avoid sorting
        x = []
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            if (abs(nums[left]) <= abs(nums[right])):
                x.append(nums[right]*nums[right])
                right = right - 1 #Reducing the right pointer after use
                
            else:
                x.append(nums[left]*nums[left])
                left = left + 1 #Increasing the left pointer after use
        
        return x[::-1] #returning the list after reversing