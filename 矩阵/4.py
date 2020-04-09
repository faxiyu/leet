class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                raw = i
                break
        colum = board[raw].index('R')

        r = ''.join(board[raw]).replace('.','')
        c = ''.join(i[colum] for i in board).replace('.','')

        return r.count("Rp") + r.count("pR") + c.count("Rp") + c.count("pR")

