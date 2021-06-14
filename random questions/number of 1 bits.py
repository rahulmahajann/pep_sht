# n=1101
# n=str(n)
# # n=list(n)
# ans=0
# for _ in n:
#     if(_=='1'):
#         ans+=1
# print(ans)
# print(n)

a,b,c,d=map(int,input().split())
aw=a/b
ah=1-aw
bw=c/d
bh=1-bw
comra=ah*bh
print(aw*(1/1-comra))