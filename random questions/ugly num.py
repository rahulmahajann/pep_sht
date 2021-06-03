a=8
if(a<=0):
    print(False)
for _ in [2,3,5]:
    while(a%_==0):
        a//=_
if(a==1):
    print(True)
else:
    print(False)