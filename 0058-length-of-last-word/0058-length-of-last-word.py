class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # the length of the entire string
        p = len(s) - 1
        
        # ignore all the trailing spaces
        while p >= 0 and s[p] == " ":
            p -= 1
            
        # now p is the index of the last character
        
        # the counter
        length = 0
        
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1
            
        return length