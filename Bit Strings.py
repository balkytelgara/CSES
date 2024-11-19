n = int(input())
z = pow(10, 9) + 7
res = 1

for i in range(n):
  res *= 2
  res %= z

print(res % z)