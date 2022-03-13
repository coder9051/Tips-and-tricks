# Start Code
# Take input fron user
a = int(input("Enter number: "))

# initialize by taking sum equal to zero
sum = 0
temp = a

# Count the length of digit
number_of_digit = len(str(a)) # length of digit

# Start loop to count sum of each digit
while temp > 0:
  x = temp%10
  b = x**(number_of_digit)
  sum += b
  temp = temp//10
  
if a == sum:
  print(a,"is Armstrong number")

else:
  print(a,"is not a Armstrong number")
