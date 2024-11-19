def div(n):
  numbers = list(range(1, n + 1))
  first_set, second_set = [], []

  for i in range(n // 2):
    if i % 2 == 0:
      first_set.append(numbers[i])
      first_set.append(numbers[n - i - 1])
    else:
      second_set.append(numbers[i])
      second_set.append(numbers[n - i - 1])
 
  return first_set, second_set
 
n = int(input())

sum_n = (n * (n + 1)) / 2

if sum_n % 2 != 0:
  print("NO")
else:
  print("YES")
 
  if n % 2 == 0:
    first_set, second_set = div(n)
  else:
    first_set, second_set = div(n - 1)

    first_set.append(n) if sum(first_set) < sum(second_set) else second_set.append(n)
  first_set, second_set = list(map(str, first_set)), list(map(str, second_set))
 
  print(len(first_set), " ".join(first_set), sep="\n")
  print(len(second_set), " ".join(second_set), sep="\n")