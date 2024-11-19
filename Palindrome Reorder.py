n = input()
s = {i: n.count(i) for i in set(n)}
 
if (len(n) % 2 and list(s.values()).count(1) > 1) or \
   (len(n) % 2 == 0 and sum([1 for i in s.values() if i % 2]) > 0):
  print("NO SOLUTION")
else:
  s = sorted(
    [(i, j) for i, j in s.items()],
    key=lambda x: x[1],
    reverse=True
  )
 
  r = ""
  center = ""
  for i, j in s:
    if j % 2 == 0:
      r += i * (j // 2)
    else:
      center = i * j
 
  print(r + center + r[::-1])