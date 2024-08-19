class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i = j = 0
        
        merged = []
        
        while i < w1 or j < w2:
            if i < w1:
                merged += word1[i]
                i += 1
            if j < w2:
                merged += word2[j]
                j += 1
                
        return "".join(merged)