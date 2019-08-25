def main():
	t = input()
	while t:
		cost = 0
		inp = map(int, raw_input().strip().split())
		n,m,k = inp[0], inp[1], inp[2]
		l = {}
		for i in xrange(k):
			inp = "-".join(raw_input().strip().split())
			l.update({inp:4})
		for i in l.keys():
			try:
				t_key = i.split("-")
				t_key[1] = str(int(t_key[1]) + 1)
				t_key = "-".join(t_key)
				if l[t_key] >= 0:
					l[i] -= 1
			except Exception as KeyError:
				pass
			try:
				t_key = i.split("-")
				t_key[1] = str(int(t_key[1]) - 1)
				t_key = "-".join(t_key)
				if l[t_key] >= 0:
					l[i] -= 1
			except Exception as KeyError:
				pass
			try:
				t_key = i.split("-")
				t_key[0] = str(int(t_key[0]) + 1)
				t_key = "-".join(t_key)
				if l[t_key] >= 0:
					l[i] -= 1
			except Exception as KeyError:
				pass
			try:
				t_key = i.split("-")
				t_key[0] = str(int(t_key[0]) - 1)
				t_key = "-".join(t_key)
				if l[t_key] >= 0:
					l[i] -= 1
			except Exception as KeyError:
				pass
		#print l
		for i,val in l.iteritems():
			cost += val
		print cost

		t -= 1


if __name__ == "__main__":
	main()

