class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer=[0]*len(seq)
        for i in range(1,len(seq)) :
            if seq[i]==seq[i-1] :
                answer[i]=abs(answer[i-1]-1)
            else :
                answer[i]=answer[i-1]
        return answer