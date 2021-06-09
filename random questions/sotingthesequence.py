s='is2 sentence4 This1 a3'
x=s.split()
n=len(x)
ans=[None]*9
for _ in x:
    # print(_)
    ans[int(_[-1])-1]=_[:-1]
print(ans)
# a=10
# for _ in range(1,a+1):
#     print(1200000*_)
# code=[1,2,3,4]
# a = code.copy()
# print(a)