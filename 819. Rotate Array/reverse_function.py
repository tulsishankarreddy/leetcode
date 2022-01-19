''' Soultion using reversing the list to achieve the rotation. Reversing is achieved by continuos swapping '''

class Solution:
    
    def reverse (self, num: List[int], low: int, high: int) -> None:
        while (low < high):
            num[low], num[high] = num[high], num[low]
            low = low + 1
            high = high - 1
            
    def rotate(self, num: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(num)
        k = k % len(num)

        self.reverse (num, 0, n-k-1)
        self.reverse (num, n-k, n-1)
        self.reverse (num, 0 , n-1)
    