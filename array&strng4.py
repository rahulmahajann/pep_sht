h= [1,8,6,2,5,4,8,3,7]
l=0
r=len(h)-1
max_ans=0
while(l!=r):
    max_ans=max(max_ans,min(h[l],h[r])*(r-l))
    if(h[l]<h[r]):
        l+=1
    else:
        r-=1
print(max_ans)