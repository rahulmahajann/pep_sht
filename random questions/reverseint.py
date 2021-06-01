x=-1
x=list(str(x))
count=0
if('-' in x):
    x.remove('-')
    count+=1

x.reverse()
# if(count!=0):
    
x=''.join(x)
x=int(x)
if(count!=0):
    x*=(-1)
if(x>2147483647 or x<-2147483648):
    print(0)
else:
    print(x)
