class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for char in "123456789":
                        if self.isValid(board, r, c, char):
                            board[r][c] = char
                            
                            # If this leads to a solution, we are done
                            if self.solve(board):
                                return True
                            
                            # Otherwise, backtrack
                            board[r][c] = "."
                    return False
        return True

    def isValid(self, board, row, col, char):
        for i in range(9):
            # Check row
            if board[row][i] == char:
                return False
            # Check column
            if board[i][col] == char:
                return False
            # Check 3x3 sub-box
            # (row // 3 * 3) finds the top row of the box
            # (i // 3) adds 0, 1, or 2 to cover all 3 rows of the box
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
                return False
        return True
