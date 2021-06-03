n=[1,0,-1,0,-2,2]
t=0
fans=[]
if(len(n)==0):
    print(fans)
n.sort()
for _ in range(len(n)):
    for i in range(_+1,len(n)):
        t_new=t-n[i]-n[_]
        left=i+1
        right=len(n)-1
        while(left<right):
            ans=[]
            rem_sum=n[left]+n[right]
            if(rem_sum<t_new):
                left+=1
            elif(rem_sum>t_new):
                right-=1
            else:
                ans.append(n[left])
                ans.append(n[right])
                ans.append(n[i])
                ans.append(n[_])
                fans.append(ans)

                while(left<right and n[left]==ans[0]):
                    left+=1
                while(left<right and n[right]==ans[1]):
                    right-=1
        while(i+1<len(n) and n[i+1]==n[i]):
            i+=1
        while(_+1<len(n) and n[_+1]==n[_]):
            _+=1
        
print(fans)