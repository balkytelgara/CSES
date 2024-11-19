n = int(input())
k = 0
 
while n >= 5:
    n //= 5
    k += n
 
print(k)