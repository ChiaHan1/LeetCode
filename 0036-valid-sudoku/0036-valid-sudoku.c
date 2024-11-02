bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    // bitmap for 9 rows, 9 columns, and 9 squares
    short bitmap_row[9] = {0};
    short bitmap_col[9] = {0};
    short bitmap_sq[9] = {0};
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (board[i][j] == '.') continue;
            // covert the ascii value to an int then subtract by 1 for shifting
            int shift = board[i][j] - '1';
            int bit = 1 << shift;
            // check the row
            if (bitmap_row[i] & bit) return false;
            bitmap_row[i] |= bit;
            // check the column
            if (bitmap_col[j] & bit) return false;
            bitmap_col[j] |=  bit;
            // check the square
            int idx = (i / 3) * 3 + (j / 3);
            if (bitmap_sq[idx] & bit) return false;
            bitmap_sq[idx] |=  bit;
        }
    }
    return true;
}