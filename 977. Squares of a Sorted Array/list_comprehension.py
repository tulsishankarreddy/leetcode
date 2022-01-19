''' We have not using sort() because it will do inplace sorting of the list and does not retuen anything. So, if we use
[x*x for x in nums].sort() the value returned will be None'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        return sorted([x*x for x in nums])  #We are using list comprehension to create a list of square
                                            #Using sorted() function we are sorting the list
                                            