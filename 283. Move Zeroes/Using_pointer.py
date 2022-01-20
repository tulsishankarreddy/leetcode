''' The solution first edits the array with non zero values from the initial postion. After updating all the
valid values at the front part of the array, rest of the array positions are filled with zeros '''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for val in nums:
            
            #updating the values at pointer potion only when we find a number expect 0
            if (val): #val != 0
                nums[pointer] = val
                pointer +=1
        
        #changes the values to 0 at the end
        for i in range(pointer, len(nums)):
            nums[i] = 0