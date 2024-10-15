class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        black = 0
        
        for c in s:
            if c == '0':
                # swap all the black balls before c
                swap += black
            else:
                # increment the number of black balls up to c
                black += 1
        
        return swap