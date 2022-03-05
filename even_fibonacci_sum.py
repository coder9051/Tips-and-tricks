
"""                                                             **Even Fibonacci Sum**
SOLUTION 1:
"""

a,b = 0,1
    s = set()
    while a+b<n:
        a,b = b, a+b
        if b%2==0:
            s.add(b)
    print(sum(s))

"""
SOLUTION 2: 
"""

n = int(input().strip())
start = 2
previous = 0
total = 2
while start < n:
  newFib = start*4 + previous
  total += newFib
  if total > n:
    total -= newFib
    break
  elif total == n:
    break
  else:
    pass
  previous = start
  start = newFib
print(total)

"""
SOLUTION 3:
"""

lista = [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074, 86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288, 117669030460994, 498454011879264, 2111485077978050, 8944394323791464, 37889062373143906]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    suma = sum([x for x in lista if x <= n])
    print(suma)
