a=[1,2]
b=[3,4]

c=a+b
c=sorted(c)
if(len(c)%2==0):
    print((c[len(c)//2]+c[(len(c)//2)-1])/2)
    print(c[len(c)//2])
    print(c[(len(c)//2)-1])
else:
    print(c[len(c)//2])
# print(a[len(a)//2])
print(c)