m=[[0,0,0],[0,1,0],[1,1,1]]
t=[[1,1,1],[0,1,0],[0,0,0]]
N = len(m) 
ans=[]
def rotate90Clockwise(arr) :
    # fans=[]
    sans=[]
    for j in range(N) :
        fans=[]
        for i in range(N - 1, -1, -1) :
            fans.append(arr[i][j])
        sans.append(fans)
    # ans.append(sans)
    # return ans
    return sans
         
# print(rotate90Clockwise(m))
cnt=0
if(m==t):
    print(True)
else:
    for _ in range(3):
        x=rotate90Clockwise(m)
        if(x==t):
            cnt+=1
            break
        else:
            m=x
if(cnt!=0):
    print(True)
else:
    print(False)


# n=[1,1,2,2,3,2]
# n=sorted(n)
# ans=0
# x=sorted(list(set(n)))
# print(x)
# for _ in range(len(x)-1,0,-1):
    
# s='1110'
# ans=0
# if(s[0]=='1'):
#     for _ in range(len(s)):
#         if(_%2==0 and s[_]=='0'):
#             ans+=1
#         elif(_%2!=0 and s[_]=='1'):
#             ans+=1
# else:
#     for _ in range(len(s)):
#         if(_%2==0 and s[_]=='1'):
#             ans+=1
#         elif(_%2!=0 and s[_]=='0'):
#             ans+=1
# print(ans)

n=[1,1,1]
n=sorted(n)
ans=0
x=sorted(list(set(n)))
for _ in range(len(x)-1,0,-1):
    l=n.index(x[_])
    ans+=(len(n)-l)
print(ans)