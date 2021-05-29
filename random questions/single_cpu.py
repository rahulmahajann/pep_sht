a="aababcabc"
ans=''
x=0
for _ in range(len(a)-2):
    for i in range(_,_+3):
        ans+=a[i]
    if(len(list(set(ans)))==3):
        x+=1
    ans=''
print(x)