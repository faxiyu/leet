class Solution(object):
    def gameOfLife(self, board):
        ds = [(-1,1), (-1,0), (-1,-1),(1, 1), (1, -1), (1, 0), (0, 1), (0, -1)]
        M, N = len(board), len(board[0])
        board_next = copy.deepcopy(board)
        for m in range(M):
            for n in range(N):
                live_count = 0
                for d in ds:
                    x=m+d[0]
                    y=n+d[1]
                    if 0<=x<M and 0<=y<N:
                        if board[x][y]==1 :
                            live_count=live_count+1
                if live_count < 2 or live_count > 3:
                    board_next[m][n]=0
                elif board[m][n] == 1 or (live_count == 3 and board[m][n] ==0):
                    board_next[m][n]=1
        for m in range(M):
            for n in range(N):
                board[m][n] = board_next[m][n]