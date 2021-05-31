s='ache'
s=list(s)
ans=[]
for _ in range(len(s)):
    if(s[_]=='a' or s[_]=='e' or s[_]=='i' or s[_]=='o' or s[_]=='u' or s[_]=='A' or s[_]=='E' or s[_]=='I' or s[_]=='O' or s[_]=='U'):
        ans.append(s[_])
for _ in range(len(s)-1,-1,-1):
    if(s[_]=='a' or s[_]=='e' or s[_]=='i' or s[_]=='o' or s[_]=='u' or s[_]=='A' or s[_]=='E' or s[_]=='I' or s[_]=='O' or s[_]=='U'):
        s[_]=ans[0]
        ans.pop(0)
print(''.join(s))