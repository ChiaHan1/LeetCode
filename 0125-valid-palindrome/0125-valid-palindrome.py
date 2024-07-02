class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left and right pointers
        i = 0
        j = len(s) - 1
        
        while i < j:
            # skipping non alphanumeric characters
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            # if the pointers are pointing at two different characters
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True