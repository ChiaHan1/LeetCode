class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        if t == "" and s != "":
            return False
        
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        
        return self.isSubsequence(s, t[1:])