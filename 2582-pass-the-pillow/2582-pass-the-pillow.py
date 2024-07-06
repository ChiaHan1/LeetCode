class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # the number of complete rounds
        rounds = time // (n - 1)
        # the remaining time afterwards
        extra = time % (n - 1)
        
        # start from the front
        if rounds % 2 == 0:
            return extra + 1
        # start from the back
        else:
            return n - extra
        