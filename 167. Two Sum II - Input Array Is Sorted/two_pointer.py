''' The solution is based on 2 pointer method. Since the array is sorted in ascending order we make use of it
by pointing 1 pointer at the start and the other at end of the array'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while (left < right):
            check = numbers[left] + numbers[right]
            if (check == target):
                return [left, right]
            
            #increase the left pointer as the summation is less and we have to move forward to increase the sum
            elif (check < target):
                left +=1
            
            #Decrease the right pointer as the summation is more and we have to move backward to decrease the sum    
            else:
                right -=1