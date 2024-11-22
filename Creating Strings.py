from itertools import permutations

n = input()
a = sorted(set(["".join(i) for i in permutations(list(n), len(n))]))

print(len(a), *a, sep="\n")