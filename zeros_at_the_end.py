# -*- coding: utf-8 -*-
"""
SOLUTION 1:
"""

def shiftAllZerosToEnd(arr):

# 'count' stores the number of non-zero element which is used to arrange non-zero elemen to the front
  count = 0

  for i in range(len(arr)):
    if arr[i] != 0:
      arr[count] = arr[i]
      count += 1

# All non-zero elements have been shifted to front and 'count' is set as index of first 0 and all elements from count to end is set to 0.
  while count < len(arr):
    arr[count] = 0
    count += 1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
shiftAllZerosToEnd(arr)
print(arr)

"""
SOLUTION 2: 
"""

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
zeroCount = arr.count(0)
for i in range(zeroCount):
  arr.remove(0)
  arr.append(0)
print(arr)

"""
SOLUTION 3: Mathematical Coder!
"""

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
arr.sort(key = bool, reverse = True)
print(arr)
