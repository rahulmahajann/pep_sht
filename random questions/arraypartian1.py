d=[1,2,3,4,5]
a={}
ans=0
for _ in d:
    if _ in a:
        ans+=a[_]
    for i in range(22):
        r=2**i-_
        if r in a:
            a[r]+=1
        else:
            a[r]=1
return ans%(10**9+7)