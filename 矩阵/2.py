class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2 :
            return 0
        count,font,len1=0,0,-1
        while(len1!=len(height) and len(height)>2):
            len1=len(height)
            a=height.index(max(height))
            if a==0 :
                b=0
            else :
                b=height.index(max(height[0:a]))
            if a < len(height)-1 :
                c=height[a+1::].index(max(height[a+1::]))+a+1
            else :
                c=a
            for x in range(b+1,c) :
                if x< a :
                    count+=height[b]-height[x]
                elif x>a :
                    count+=height[c]-height[x]
            for _ in range(b+1,c):
                height.pop(b+1)
            if a==b and len(height)>2:
                height.pop(0)
            if a==c and len(height)>2:
                height.pop(len(height)-1)
            if  len(height)==len1 and font==0 :
                font=1
                len1-=1
        return count