class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        
        while numBottles >= numExchange:
            # maximum number of times can consume numExchange number
            # of bottles using numBottles
            exchange = numBottles // numExchange
            
            total += numExchange * exchange
            numBottles -= numExchange * exchange
            
            numBottles += exchange
        
        return total + numBottles