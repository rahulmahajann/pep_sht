a=str(231)
b=[]
for _ in range(len((a))):
    b.append(int(a[_]))
grt=-1
ind=-1
ind2=-1
justbada=1000000000

if(len(a)==1):
    print(-1)
elif(len(b)==2):
    x=a[::-1]
    if(int(x)>int(a)):
        print(x)
    else:
        print(-1)
else:


    for _ in range(len(b)-2,0,-1):
        if(b[-1]>b[_]):
            grt=b[_]
            ind=_
            break
    if(grt==-1):
        print(-1)
    else:

        for _ in range(_+1,len(b)):
            if(b[_]>grt):
                justbada=min(justbada,b[_])
                ind2=_
                break

        b[ind],b[ind2]=b[ind2],b[ind]


        c=[]
        d=[]
        d=b[0:ind+1]
        c=b[ind+1:]
        c=sorted(c)
        e=d+c
        f=[]
        for _ in e:
            f.append(str(_))
        g=''.join(f)
        if(g==a):
            print(-1)
        else:
            print(g)