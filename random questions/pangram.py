class Solution:
    def checkIfPangram(self, s: str) -> bool:
        a=list(s)
        b=list(set(a))
        if(len(b)==26):
            return True
        else:
            return False