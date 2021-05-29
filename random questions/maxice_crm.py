costs = [1,3,2,4,1]
coins=7
ans=0
if(min(costs)>coins):
    print(0)
elif(sum(costs)<=coins):
    print(len(costs))
else:
    costs=sorted(costs)
    for _ in costs:
        if(coins-_>=0):
            ans+=1
            coins-=_
    print(ans)
