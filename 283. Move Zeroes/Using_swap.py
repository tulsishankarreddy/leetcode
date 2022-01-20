''' The solution swaps when it first a non zero value in the array. We also use a fast & slow pointer here 
in te form of i and j'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
                if(nums[i]): #nums[i] != 0
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1