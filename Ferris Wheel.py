n, x = map(int, input().split())
weights = sorted(map(int, input().split()))
count = 0
i, j = 0, n - 1
 
while i <= j:
	if weights[i] + weights[j] <= x:
		i += 1
		j -= 1
		count += 1
	else:
		j -= 1
		count += 1
 
print(count)