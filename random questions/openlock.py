deadends=["0201","0101","0102","1212","2002"]
target='0202'
deadends = set(deadends)
if "0000" in deadends: 
    print(-1)
if target == "0000": 
    print(0)
import collections
queue = collections.deque()
visited = {}
queue.append(["0000", 0])
while len(queue) > 0:   
    current, level = queue.popleft()    
    new_nums = []       
    for i in range(4):
        new_nums.append(current[:i] + str((int(current[i]) + 1) % 10) + current[i+1:])                
        new_nums.append(current[:i] + str((int(current[i]) - 1) % 10) + current[i+1:])
    for num in new_nums:
        if num in visited or num in deadends:
            continue
        visited[num] = True                
        if num == target:
            print(level+1)
        queue.append([num, level + 1])                
print(-1)