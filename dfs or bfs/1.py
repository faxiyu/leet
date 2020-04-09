class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        count=1
        z=[[0]*n for i in range(m)]
        z[0][0]=1
        for i in range(m) :
            for j in range(n):
                s=0
                if i>=10 :
                    s+=int(str(i)[0])+int(str(i)[1])
                else :
                    s+=i
                if j >=10 :
                    s+=int(str(j)[0])+int(str(j)[1])
                else :
                    s+=j
                if s<=k :
                    if  j-1>=0 :
                        if z[i][j-1] ==1 :
                            count+=1
                            z[i][j]=1
                            continue
                    if  i-1>=0 :
                        if z[i-1][j] ==1 and z[i][j]==0:
                            count+=1
                            z[i][j]=1
                            continue
        return count