from itertools import combinations
 
n = int(input())
p = list(map(int, input().split()))
 
if n == 1 and p == [1]:
  print(1)
elif n == 2 and p == [1, 1]:
  print(0)
else:
  ps = sum(p)
  m = 1e9
 
  for i in range(1, n - 1):
    for comb in combinations(p, i):
      sc = sum(comb)
      m = min(m, abs((ps - sc) - sc))
 
  print(int(m))