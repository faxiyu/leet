class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        b=[0]*(max(deck)+1)
        for i in deck:
            b[i]=b[i]+1
        max1=max(b)+1
        for j in range(2,max1):
            sum1=0
            for i in b:
                if i % j !=0:
                    sum1=1
                    break
            if sum1==0:
                return True
        return False