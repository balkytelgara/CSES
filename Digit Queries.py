q = int(input())

for _ in range(q):
  k = int(input())
  i, e = 0, 1

  while i <= pow(10, e) and i < k:
    if i <= pow(10, e + 1) and i < k:
      i += e + 1
    else:
      e += 1
  
  print(i)