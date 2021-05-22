class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num=list(set(nums))
        ans=[]
        for _ in num:
            if(nums.count(_)>len(nums)//3):
                ans.append(_)
        return ans



# Approach 2


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1=None
        elem2=None
        count1=0
        count2=0
        for _ in nums:
            if(elem1!=None and elem1==_):
                count1+=1
            elif(elem2!=None and elem2==_):
                count2+=1
            elif(count1==0):
                elem1=_
                count1+=1
            elif(count2==0):
                elem2=_
                count2+=1
            else:
                count1-=1
                count2-=1
        ans=[]
        if(nums.count(elem1)>(len(nums)//3)):
            ans.append(elem1)
        if(nums.count(elem2)>(len(nums)//3)):
            ans.append(elem2)
        
        return ans