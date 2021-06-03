f='aaaa'
s='baa'

if(len(s)==0):
    print(0)
if(len(f)<len(s)):
    print(-1)
else:
    for _ in range(len(f)):
        if(f[_:_+len(s)]==s):
            print(_)
            break
    print(-1)