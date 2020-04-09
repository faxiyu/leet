class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ludi=[(i,j) for i in range(n) for j in range(n)  if grid[i][j]==1]
        step=-1
        if len(ludi)==0 or len(ludi)==n*n :
            return step
        while(len(ludi)>0):
            n1=len(ludi)
            for _ in range(n1):
                lx,ly=ludi.pop(0)
                for x,y in ((lx+1,ly),(lx-1,ly),(lx,ly+1),(lx,ly-1)):
                    if x>=0 and x<n and y>=0 and y<n and grid[x][y]==0:
                        grid[x][y]=-1
                        ludi.append((x,y))
            step+=1
        return step