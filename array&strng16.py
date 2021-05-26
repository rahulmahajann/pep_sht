for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=c*b
    max1=d[0]
    max2=d[0]
    for _ in range(1,len(d)):
        max1=max(d[_],d[_]+max1)
    
        if(max1>max2):
            max2=max1
    
    print(max2)