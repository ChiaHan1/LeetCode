bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    // bitmap for 9 rows, 9 columns, and 9 squares
    uint16_t bitmap_row[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    uint16_t bitmap_col[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    uint16_t bitmap_sq[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (board[i][j] == '.') continue;
            // covert the ascii value to an int
            int num = board[i][j] - '0';
            // check the row
            if (bitmap_row[i] & (1 << num)) return false;
            bitmap_row[i] |= (1 << num);
            // check the column
            if (bitmap_col[j] & (1 << num)) return false;
            bitmap_col[j] |= (1 << num);
            if (bitmap_sq[(i / 3) * 3 + (j / 3)] & (1 << num)) return false;
            bitmap_sq[(i / 3) * 3 + (j / 3)] |= (1 << num);
        }
    }
    return true;
}