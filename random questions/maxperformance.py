from heapq import heappop,heapify,heappush

speed=[2,10,3,1,5,8]
e=[5,4,3,9,7,2]
k=2
ar=[]
heapify(ar)

ans=0
sp=0

fans=[]

for _ in range(len(speed)):
    fans.append([e[_],speed[_]])

fans.sort(key=lambda i: -i[0])

for ef,spe in fans:
    heappush(ar,spe)
    sp+=spe

    if(len(ar)>k):
        sp-=heappop(ar)
    
    # if(len(ar)>k):


    ans=max(ans,sp*ef)

print(ans%(10**9+7))