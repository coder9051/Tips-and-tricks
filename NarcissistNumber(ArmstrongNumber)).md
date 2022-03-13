# Narcissist Number/ Armstrong number
In number theory, a narcissistic number (also known as a pluperfect digital invariant (PPDI), an Armstrong number (after Michael F. Armstrong) or a plus perfect number) in a given number base b is a number that is the sum of its own digits each raised to the power of the number of digits.

## Algorithm
Here is algorithm to check whether a number is Armstrong number or not.

 1. The number of digits in num is determined and found out.

 2. The sum of digits of a number in Python or individual digit sums are got by performing num mod 10, where mod is called the remainder operation.

 3. The individual digit is then raised to the power (number of digits) and stored.

 4. The number is then divided by 10 in order to obtain the second digit.

 5. All the above 3-steps numbered Steps 2, 3 and 4 are performed until the value of num is greater than 0.

 6. When the number is less than 0, end the while loop.

 7. Check the sum obtained or Armstrong value is the same as the original number

 8. When yes, the number is labelled an Armstrong number
 
 ## Python Code
 
 ```python
 a = int(input("Enter number: "))
sum = 0
temp = a
number_of_digit = len(str(a)) # length of digit
while temp > 0:
  x = temp%10
  b = x**(number_of_digit)
  sum += b
  temp = temp//10
print(sum)
if a == sum:
  print(a,"is Armstrong number")
else:
  print(a,"is not a Armstrong number")
 ```
 ## Conclusion
Beginners often wonder what is Armstrong number aka the narcissist number. It is of special interest to new programmers and those learning a new programming language because of the way the number behaves in a given number base.

There are only 89 narcissistic numbers in base 10, of which the largest with 39 digits is
 
         115,132,219,018,763,992,565,095,597,973,971,522,401 
