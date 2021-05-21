class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for _ in nums:
            ans.append(_*_)
        return sorted(ans)