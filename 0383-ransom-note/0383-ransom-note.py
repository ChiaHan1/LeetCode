from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = defaultdict(int)
        
        for c in magazine:
            alphabet[c] += 1
                        
        for c in ransomNote:
            if alphabet[c] == 0:
                return False
            else:
                alphabet[c] -= 1
        return True