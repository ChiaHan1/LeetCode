class Solution:
    def isHappy(self, n: int) -> bool:
        # a set of seen numbers
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            # generate the new number
            new_num = 0
            while n > 0:
                n, d = divmod(n, 10)
                new_num += d ** 2
            n = new_num
        
        return n == 1
            