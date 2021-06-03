import math
ans=[]
def primeFactors(n):	
    # ans.append()
	while n % 2 == 0:
		ans.append(2)
		n = n//2
	for i in range(3,int(math.sqrt(n))+1,2):
		while n % i== 0:
			ans.append(i)
			n = n // i
	# if n > 2:
	# 	ans.append(n)
    # ans.append
	return ans

nu=[21,4,7]
fans=[]
for _ in nu:
    primeFactors(_).append(_)
    if(len(set(primeFactors(_)))==3):
        for _ in set(primeFactors(_)):
            fans.append(_)
        fans.append(1)
        primeFactors(_).clear()
    else:
        primeFactors(_).clear()
print(fans)
# print(primeFactors(21))