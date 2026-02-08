class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = defaultdict(set) # key is row index
        colmap = defaultdict(set)
        sqmap = defaultdict(set) # key is r,c tuple // 3

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rowmap[r] or
                    board[r][c] in colmap[c] or
                    board[r][c] in sqmap[(r//3,c//3)]):
                    return False; 

                rowmap[r].add(board[r][c])
                colmap[c].add(board[r][c])
                sqmap[(r//3,c//3)].add(board[r][c])

        return True        


        