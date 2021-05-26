def soe(n):
    ans=[]
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            ans.append(p)

    return ans

for _ in range(int(input())):
    a,b=map(int,input().split())
    l=soe(b)
    for _ in l:
        if(_>=a):
            print(_)