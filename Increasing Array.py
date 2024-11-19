n = int(input())
x = list(map(int, input().split()))
 
k = 0
 
for i, j in enumerate(x):
    if i == 0:
        pass
    elif j <= x[i - 1]:
        diff = x[i - 1] - j
        k += diff
        x[i] = j + diff
 
print(k)