a=[3,3]
t=6
ar=[]
for _ in range(len(a)):
    ans=t-a[_]
    a[_]='x'
    ar.append(_)
    if(ans in a):
        ar.append(a.index(ans))
        break
    else:
        ar.clear()
print(ar)