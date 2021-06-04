n=19
fans=[]
while(n>1):
    ans=0
    for _ in str(n):
        ans+=int(_)**2
    n=ans
    if(n not in fans):
        fans.append(n)
    else:
        print(False)
print(True)


# sq=0
# def x(n):
#     while(n!=0):
#         r = n//10
#         sq += r**2
#         n=n/10
#     return sq

# def ishappy(n):


#     if(x(n)==1):
#         print(1)
#     else:
#         x(sq)