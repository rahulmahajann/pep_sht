j1=1
j2=2
t=3

a,b=j1,j2
while(j2):
    c=j1%j2
    j1=j2
    j2=c
if(not t or (j1 and t<=a+b and not t%j1)):
    print(True)
else:
    print(False)