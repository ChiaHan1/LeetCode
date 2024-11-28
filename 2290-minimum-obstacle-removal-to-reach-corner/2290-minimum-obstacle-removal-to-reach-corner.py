class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        min_obstacles = [[float('inf')] * n for _ in range(m)]
        
        # bfs
        frontier = [[0, 0]]
        # the starting point
        min_obstacles[0][0] = grid[0][0]
        
        while frontier:
            # current node
            current = frontier.pop()
            # the neighbors of the current node
            neighbors = [(current[0] + h, current[1] + v) for h, v in actions]
            # for each neighbor
            for nr, nc in neighbors:
                # boundary check
                if (0 <= nr < m) and (0 <= nc < n):
                    # check whether the neighbor has been explored
                    if min_obstacles[nr][nc] == float('inf'):
                        if grid[nr][nc] == 1:
                            # add 1 to the minimum obstacle to 
                            min_obstacles[nr][nc] = min_obstacles[current[0]][current[1]] + grid[nr][nc]
                            # insert to the back of the frontier
                            frontier.insert(0, (nr, nc))
                        else:
                            # the minimum obstacle remains the same
                            min_obstacles[nr][nc] = min_obstacles[current[0]][current[1]]
                            # insert to the front of the frontier
                            frontier.append((nr, nc))
                        
                        if nr == m - 1 and nc == n - 1:
                            return min_obstacles[m - 1][n - 1]
                        
        return min_obstacles[m - 1][n - 1]