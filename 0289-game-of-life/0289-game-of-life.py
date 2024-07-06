class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # dimension of the board
        m, n = len(board), len(board[0])
        
        # all the neighboring cells
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # iterate through the board
        for i in range(m):
            for j in range(n):
                # number of alive neighbors
                alive_neighbors = 0
                # for each neighbor's offset
                for r, c in neighbors:
                    row = i + r
                    col = j + c
                    # if the cell is valid and alive
                    if (row < m and row >= 0) and (col < n and col >= 0) and abs(board[row][col]) == 1:
                        alive_neighbors += 1
                # rule 1 or rule 3
                if board[i][j] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                    # indicate the cell is now dead but was alive
                    board[i][j] = -1
                # rule 4
                if board[i][j] == 0 and alive_neighbors == 3:
                    # indicate the cell is now alive but was dead
                    board[i][j] = 2
                    
        # update the board
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            
                
                