class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0

        # points visited
        visited = {(0, 0)}

        for direction in path:
            if direction == 'E':
                x += 1
            if direction == 'S':
                y -= 1
            if direction == 'W':
                x -= 1
            if direction == 'N':
                y += 1
            
            # if current position has been visited
            if (x, y) in visited:
                return True
            
            visited.add((x, y))
        
        return False