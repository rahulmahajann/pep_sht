class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        ans=0
        maxl,maxr=0,0
        while(l<=r):
            if(h[l]<=h[r]):
                if(h[l]>=maxl):
                    maxl=h[l]
                else:
                    ans+=maxl-h[l]
                l+=1
            else:
                if(h[r]>=maxr):
                    maxr=h[r]
                else:
                    ans+=maxr-h[r]
                r-=1
        return ans