class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        maxi=0
        summ=0
        count=0
        for _ in n:
            if(_<0):
               count+=1 
            summ+=_
            if(summ<0):
                summ=0
            maxi=max(summ,maxi)
        if(count==len(n)):
            return sorted(n)[-1]
        else:
            return maxi