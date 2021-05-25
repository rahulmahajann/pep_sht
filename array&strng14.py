class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        n=sorted(n)
        return max(n[0]*n[1]*n[-1] , n[-1]*n[-2]*n[-3])