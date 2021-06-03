x=2.10000
n=3
if(n%2==0):
    print((x*x)**(n//2))
else:
    print(x*((x*x)**((n-1)//2)))
# import math
# logpart=math.log2(x)
# print(n*logpart)