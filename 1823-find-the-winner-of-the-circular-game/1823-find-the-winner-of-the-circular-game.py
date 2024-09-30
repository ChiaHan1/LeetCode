class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = deque(range(1, n + 1))
        
        while len(circle) > 1:
            # process the first k - 1 friends without eliminating them
            for _ in range(k - 1):
                circle.append(circle.popleft())
                
            # eliminate the k th friend
            circle.popleft()
            
        return circle[0]