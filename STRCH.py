t = input()
for i in range(t):
	n = input()
	s = raw_input().strip().split()
	total = 0
	last = 0
	for i in range(n):
		if s[0][i] == s[1]:
			t1 = i + 1 -last
			total += t1 + ((n - i - 1) * t1 )
			last = i + 1  
	print total 