s='()'
arr=[]
dic={
    ']':'[',
    '}':'{',
    ')':'('
}
for _ in s:
    if _ in dic.values():
        arr.append(_)
    elif _ in dic.keys():
        if arr==[] or dic[_]!=arr.pop():
            print(False)
    else:
        print(False)
print(arr==[])