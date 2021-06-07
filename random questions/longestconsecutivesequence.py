n=[1,200,2,3,4,100]
n=sorted(n)
ans=0
fans=0
if(len(n)==0):
    print(0)
for _ in range(len(n)-1):
    if(n[_+1]-n[_]==1):
        ans+=1
        fans=max(ans,fans)
    else:
        # fans=max(ans,fans)
        ans=0
    # ans=
print(fans+1)