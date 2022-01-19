''' This can be solved using the slicing method used in list. We have to modify the list by take moving the
last part of the array in reverse order and joining it with the remaining part of the list to its right'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)  #To reduce the a full cycle rotation
        nums[:] = nums[-k:] + nums[:-k] #nums[-k:] -> end part of the list in reverse order
                                        #nums[:-k] -> front part of the list which is attached to the right of nums[-k:]