t=12
import math
t=abs(t)
n=math.floor(math.sqrt(t))
while 1:
    d=(n*(n+1))//2-t
    print(d)
    if d>=0:
        if d%2==0:
            print(n)
    n+=1