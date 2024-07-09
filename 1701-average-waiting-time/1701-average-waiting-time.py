class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle = 0
        net_wait = 0
        
        for c in customers:
            # the next idle time is given by the time of delivery of current customer's order
            next_idle = max(c[0], next_idle) + c[1]
            
            # wait time for the current customer
            net_wait += next_idle - c[0]

        return net_wait / len(customers)