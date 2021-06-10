n=[2,7,11,15]
t=9

ans=[]
for _ in range(len(n)):
    r=abs(t-n[_])
    if(r in n):
        ans.append(_+1)
        ans.append(n.index(r)+1)
        break
print(ans)