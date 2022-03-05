"""
SOLUTION 1: 
"""

arr = [1, 4, 2, 3, 4, 5]
n = len(arr) - 1 #It is also equal to max of list.
sumArr = sum(arr)
originalSum = (n*(n+1))//2
repeatingElement = sumArr - originalSum
print(repeatingElement)

"""
SOLUTION 2: 
"""

def findRepeating(arr, n):
    s = set()
    for i in range(n):
        if arr[i] in s:
            return arr[i]
        s.add(arr[i])
     
    # If input is correct, we should
    # never reach here
    return -1
 
arr = [9, 8, 2, 6, 1, 8, 5, 3]
n = len(arr)
print(findRepeating(arr, n))

"""
SOLUTION 3:
"""

def findRepeating(arr, n):
     
    res = 0
    for i in range(0, n-1):
        res = res ^ (i+1) ^ arr[i]
    res = res ^ arr[n-1]
         
    return res

arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
n = len(arr)
print(findRepeating(arr, n))

"""
SOLUTION 4:
"""

ef repeatingElement(arr):
  for i in range(len(arr)):
   # to get the value of the current element 
    if arr[i] < 0:
      val = -arr[i]

   # make element at index `val` negative if it is positive
    else:
      val = arr[i]

   # if the element is already negative, it is repeated
    if arr[val] > 0:
      arr[val] = - arr[val]
    else:
      repeatedElement = val
      break

  # restore the original list before returning 
  for i in range(len(arr)):
    if arr[i] < 0:
      arr[i] = -arr[i]

  return repeatedElement

nums = [1, 2, 3, 4, 2]
print(repeatingElement(nums))
