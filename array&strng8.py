class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num=list(set(nums))
        ans=[]
        for _ in num:
            if(nums.count(_)>len(nums)//3):
                ans.append(_)
        return ans



        # cr