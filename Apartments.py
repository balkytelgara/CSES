def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    l1, l2, c = 0, 0, 0
    while l1 < n and l2 < m:
        if abs(a[l1] - b[l2]) <= k:
            c += 1
            l1 += 1
            l2 += 1
        else:
            if a[l1] > b[l2]:
                l2 += 1
            else:
                l1 += 1
    print(c)
 
solve()