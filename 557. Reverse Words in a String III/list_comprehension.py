''' Solution using string comprehension for reversing the letters in words'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words=[i[::-1] for i in words]
        s=' '.join(words)
        return s