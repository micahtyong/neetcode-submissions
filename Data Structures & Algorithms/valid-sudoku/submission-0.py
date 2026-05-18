# This is not solving sudoku, this is just checking if the board, as is, is valid.
# Naive: 3 checks
# 1. All rows, O(mn), sq grid => O(n^2)
# 2. All columns, O(mn)
# 3. All grids, O(mn)
# Iterate through each element and see if something (not ".") was repeated before. If so, return false.
# Runtime: O(3mn) = O(mn)
# Space: O(mn) worst case

EMPTY_CHAR = "."

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.checkRow(board, i): return False

        for j in range(len(board[0])):
            if not self.checkCol(board, j): return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not self.checkGrid(board, i, j): return False
        
        return True
    
    def checkRow(self, board, i) -> bool:
        s = set()
        for elem in board[i]:
            if elem in s and elem != EMPTY_CHAR:
                return False
            s.add(elem)
        return True
    
    def checkCol(self, board, j) -> bool:
        s = set()
        for i in range(len(board)):
            elem = board[i][j]
            if elem in s and elem != EMPTY_CHAR:
                return False
            s.add(elem)
        return True

    def checkGrid(self, board, start_i, start_j) -> bool:
        # Upper left corner point of grid
        s = set()
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                elem = board[i][j]
                if elem in s and elem != EMPTY_CHAR:
                    return False
                s.add(elem)
        return True



