t = int(input())
l = []
for i in range(t):
	x, y = map(int, input().split())
	l.append((x, y))
 
for x, y in l:
	maxv = max([x, y])
	sq = (maxv - 1 ) * (maxv - 1)
 
	if maxv % 2 == 0:
		if y > x:
			print(sq + x)
		else:
			print(maxv * maxv - y + 1)
	else:
		if y > x:
			print(maxv * maxv - x + 1)
		else:
			print(sq + y