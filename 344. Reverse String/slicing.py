''' The solutions uses the method of string slicing '''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[: : -1] #s = s[: : -1] will not give you correct answer
            