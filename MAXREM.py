n = input()
l = map(int,raw_input().strip().split())
max1 = 0 
max2 = 0
for i in l:
	if max1 < i:
		max2 = max1
		max1 = i
print max2%max1