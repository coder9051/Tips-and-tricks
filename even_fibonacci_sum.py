
"""                                                             **Even Fibonacci Sum**

The Fibonacci sequence was first found by an Italian named Leonardo Pisano Bogollo (Fibonacci). 
Fibonacci numbers are a sequence of whole numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... This infinite sequence is called the Fibonacci sequence. 
Here each term is the sum of the two preceding ones, starting from 0 and 1. This has been termed "nature's secret code".
Every third term of this series is even.... and the series of even terms goes like 0,2,8,34,... so any even term E(n)can be expressed as E(n)= 4*E(n-1) + E(n-2).... i.e. if you check the series 0, 1, 2, 3, 5, 8 which is the fibinoacci series every third term is even and the next even term sequence can be caluclated using 4 * (8) + 2 which is 4*(n-3) + (n- 6).

SOLUTION 1:
Using Simple approach of adding even number. But this would not work for time restricted and space restricted question.
"""

a,b = 0,1
    s = set()
    while a+b<n:
        a,b = b, a+b
        if b%2==0:
            s.add(b)
    print(sum(s))

"""SOLUTION 2: This question actually has an easy logic. Lets the fibonacci series:1 1 2 3 5 8 13 21 34 55 89 144
Now separate the even numbers :- 2 8 34 144

          8 = 2*4 + 0
         34 = 8*4 + 2
        144 = 34*4 + 8
        610 = 144*4 + 34

GENERAL FORM
beginning = 2
previous = 0
IN LOOP:
(next_even) = beginning * 4 + previous
//calcuate sum
previous = beginning
beginning = next_even
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

"""SOLUTION 3:
This is a trick I learned when in a contest, since there was a problem that had to be solved this way due to time restrictions.
Since the problem is so fixed (only Fibonacci numbers) and bounded (n < 4e16), you can precompute all even Fibonacci numbers and just put them in code, resulting in a very efficient solution.

An even more efficient answer would be to precompute every sum up to a certain even Fibo number, avoiding the sum of large numbers. Finally, a last improvemnt would be finding which if the previous precomputed sums is the correct one. That can be done with a certain formula that involves the golden ratio. This makes this problem solvable in constant time.
"""

lista = [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074, 86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288, 117669030460994, 498454011879264, 2111485077978050, 8944394323791464, 37889062373143906]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    suma = sum([x for x in lista if x <= n])
    print(suma)

"""Just wanted to share some more information which I found intersting.
1) Sum of the first N Fibonacci numbers always equals to F(N+2)-1
2) Every 3d Fibonaccy number is even and this even Fib is a sum of two preceeding odd Fibs.
3) So sum of the sequence of all even Fibonacci numbers less than even Fibonacci number with index E equals to the sum of all Fibonacci numbers up to E, divided by 2, so it is (F(E+2)-1)/2
In this task if you want to employ Binet's formula, make sure you use phi and sqrt(5) constants with at least 40-42 decimal digits (google for their values), that means you can not use double precision, you need 128 bits.
"""
