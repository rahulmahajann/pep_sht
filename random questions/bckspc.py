s='ab##'
t='c#d#'

# a#cc
a,b=[],[]

for _ in s:
    if not a and _=='#':
        continue
    elif _=='#':
        a.pop()
    else:
        a.append(_)
for _ in t:
    if not b and _=='#':
        continue
    elif _=='#':
        b.pop()
    else:
        b.append(_)

print(''.join(a)==''.join(b))


# # print(a)
# # print(not a)

# #  def backspaceCompare(self, s: str, t: str) -> bool:
# # i = 0
# # j = 0
# # s = list(s)
# # t = list(t)
# # while(i<len(s) and j<len(t)):
# #     if(s[i]=="#"):
# #         s.pop(i-1)
# #     elif(t[j]=="#"):
# #         t.pop(j-1)
# #     i+=1
# #     j+=1
# # if(s==t):
# #     print(1)
# # else: 
# #     print(0)
        

# n=[0,0,1,2,54]
# a=n.count(0)
# for _ in range(a):
#     n.remove(0)
# n=sorted(n)
# for _ in range(a):
#     n.append(0)
# print(n)