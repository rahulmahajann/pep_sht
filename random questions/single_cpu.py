d='234'
listi=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        # for _ in digits:
if(len(d)==0):
    print([])
elif(len(d)==1):
    import itertools

    # a=['a','b','c']
    # b=['a','b','c']
    # c=['a','b','c']
    ans=[]
    a=d[0]
    # print(list(itertools.product(a,b,c)))
    for _ in list(itertools.product(listi[int(a)-2])):
        ans.append(''.join(_))
    print(ans)
elif(len(d)==2):
    import itertools
    a=d[0]
    b=d[1]
    # a=listi[d[0]-2]   
    # b=listi[d[1]-2]
    # a=['a','b','c']
    # b=['a','b','c']
    # c=['a','b','c']
    ans=[]
    # print(list(itertools.product(a,b,c)))
    x=list(itertools.product(listi[int(a)-2],listi[int(b)-2]))
    for _ in x:
        ans.append(''.join(_))
    print(ans)
elif(len(d)==3):
    import itertools
    a=d[0]
    b=[1]
    c=[2]
    # a=['a','b','c']
    # b=['a','b','c']
    # c=['a','b','c']
    ans=[]
    # print(list(itertools.product(a,b,c)))
    for _ in list(itertools.product(listi[int(a)-2],listi[int(b)-2],listi[int(c)-2])):
        ans.append(''.join(_))
    print(ans)
else:
    import itertools
    a=[0]
    b=[1]
    c=[2]
    d=[3]
    # a=['a','b','c']
    # b=['a','b','c']
    # c=['a','b','c']
    ans=[]
    # print(list(itertools.product(a,b,c)))
    for _ in list(itertools.product(listi[int(a)-2],listi[int(b)-2],listi[int(c)-2],listi[int(d)-2])):
        ans.append(''.join(_))
    print(ans)