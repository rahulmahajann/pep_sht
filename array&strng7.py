class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=list(set(nums))
        ans=len(nums)//2
        for _ in num:
            if(nums.count(_)>ans):
                return _