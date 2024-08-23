# for regular expression
import re
# to use gcd for reduction
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # numerator and denominator
        num = 0
        denom = 1
        
        # separate expression
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))
        
        for i in range(0, len(nums), 2):
            # numerator and denominator of current fraction
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])
            
            num = (num * curr_denom) + (curr_num * denom)
            denom = denom * curr_denom
            
        # fraction reduction
        gcd = math.gcd(num, denom)
        num //= gcd
        denom //= gcd
        
        return str(num) + "/" + str(denom)
            