class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        for _ in typed:
            if(i<len(name) and _==name[i]):
                i+=1
            elif(i>0 and _==name[i-1]):
                continue
            else:
                return False
        if(i==len(name)):
            return True
        else:
            return False
            