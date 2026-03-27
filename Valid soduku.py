from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use sets to store digits seen in each row, column, and sub-box
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Identify the current 3x3 box
                box_idx = (r // 3, c // 3)
                
                # Check for duplicates in the current row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Add value to the sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
