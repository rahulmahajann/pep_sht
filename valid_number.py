a=".1"
dig=False
e=False
dot=False
count=0

for _ in range(len(a)):
    if(a[_].isdigit()):
        dig=True
    elif(a[_]=='+' or a[_]=='-'):
        if(count>=2):
            print('false')
        if(_>0 and (a[_-1]!='e' and a[_-1]!='E')):
            print('false')
        if(_==len(a)-1):
            print('false')
        count+=1
    elif(a[_]=='.'):
        if(dot or e):
            print('false')
        if(_==len(a)-1 and (not dig)):
            print('false')
        dot=True
    elif(a[_]=='e' or a[_]=='E'):
        if(e or (not dig) or _==len(a)-1):
            print('false')
        e=True
    else:
        print('false')

print('true')