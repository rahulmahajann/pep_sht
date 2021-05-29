a='111000'
c1=0
c2=0
if(a.count('0')==a.count('1')):
    for _ in range(len(a)):
        if(_%2!=0 and a[_]=='0'):
            c1+=1
        if(_%2==0 and a[_]=='1'):
            c1+=1
        if(_%2!=0 and a[_]=='1'):
            c2+=1
        if(_%2==0 and a[_]=='0'):
            c2+=1
    print(min(c1,c2))
    print(c1,c2)
else:
    print(-1)