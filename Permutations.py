n = int(input())
 
a = [
    *range(2, n + 1, 2),
    *range(1, n + 1, 2)
]
 
for index, value in enumerate(a):
    if index != 0:
        if a[index - 1] == value + 1 or \
           a[index - 1] + 1 == value:
            print("NO SOLUTION")
            break
else:
    print(*a)