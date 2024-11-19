length = int(input())
n = list(map(int, input().split()))
total = 0
for i in range(2, len(n) + 2):
	total += i
	total -= n[i - 2]
print(total + 1)