n = int(input())
p = sorted(map(int, input().split()))
ans = 0

for i in range(n):
  ans += abs(p[n // 2] - p[i])

print(ans)