a=[]
b=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
for _ in b:
    if(_=='+' or _=='-' or _=='*' or _=='/'):
        s=int(a.pop())
        f=int(a.pop())
        if(_=='+'):
            a.append(f+s)
        elif(_=='-'):
            a.append(f-s)
        elif(_=='*'):
            a.append(f*s)
        elif(_=='/'):
            a.append(int(f/s))
    else:
        a.append(int(_))

ans=a.pop()
print(ans)

