n=10
a=[]
for _ in range(1,n+1):
    a.append(_)
for _ in range(len(a)):
    if(_%2!=0):
        temp=a[_-1]
        a[_-1]=a[_]
        a[_]=temp
print(a)