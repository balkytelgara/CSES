for _ in range(int(input())):
    a, b = map(int, input().split())
 
    a, b = (b, a) if b > a else (a, b)
    
    if a > b * 2 or (a + b) % 3 != 0:
        print("NO")
    else:
        print("YES")