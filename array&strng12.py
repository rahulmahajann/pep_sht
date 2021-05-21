class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        ans=1
        for _ in A:
                if(_==0):
                    continue
                else:
                    ans*=_
        
        arr=[]
            
        if(A.count(0)>1):
            for _ in range(len(A)):
                arr.append(0)
        elif(A.count(0)==1):
            for _ in A:
                if(_!=0):
                    arr.append(0)
                else:
                    arr.append(ans)
        else:
            for _ in A:
                arr.append(ans//_)
                
        
        return arr