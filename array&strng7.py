class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=list(set(nums))
        ans=len(nums)//2
        for _ in num:
            if(nums.count(_)>ans):
                return _


# APPROACH 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=nums[0]
        count=1
        for _ in range(1,len(nums)):
            if(m==nums[_]):
                count+=1
            else:
                count-=1
                if(count==0):
                    count=1
                    m=nums[_]
        return m