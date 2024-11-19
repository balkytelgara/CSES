a = input()
 
rep = set()
 
current = a[0]
k = 1
 
for char in a[1:]:
    if char == current:
        k += 1
        current = char
    else:
        rep.add(k)
        current = char
        k = 1
 
if k > 1:
    rep.add(k)
 
try:
    print(max(rep))
except:
    print(1)