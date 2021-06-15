c=[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
x=c[0][0]
y=c[0][1]
ans=[]
for _ in range(1,len(c)):
    ans.append((y-c[_][1])//(x-c[_][0]))
    print(ans)
if(len(set(ans))==1):
    print(1)
else:
    print(0)