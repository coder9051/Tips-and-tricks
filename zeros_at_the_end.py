# -*- coding: utf-8 -*-
"""
                                       **Move all zeros present in an array to the end**

Q. Given an integer array, move all zeros present on it to the end. The solution should maintain the relative order of items in the 
array and should not use constant space.

There can be many ways to solve this problem. Following is a simple and interesting way to solve this problem. 


SOLUTION 1:
Traverse the given array ‘arr’ from left to right. While traversing, maintain count of non-zero elements in array. Let the count be ‘count’. For every non-zero element arr[i], put the element at ‘arr[count]’ and increment ‘count’. After complete traversal, all non-zero elements have already been shifted to front end and ‘count’ is set as index of first 0. Now all we need to do is that run a loop which makes all elements zero from ‘count’ till end of the array.
Below is the implementation of the above approach. 

The time complexity of the this solution is O(n), where n is the size of the input. 
Auxillary space is O(1)
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
SOLUTION 2: Coders trick
First we count number of zeros then we iterate through array and remove all the zeros and append zeros at the end of array for every zeros removed.
Time complexity of this solution is greater then O(n) but no extra space is required.

"""

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
zeroCount = arr.count(0)
for i in range(zeroCount):
  arr.remove(0)
  arr.append(0)
print(arr)

"""
SOLUTION 3: Mathematical Coder!
Sort the array by setting key to bool and reverse is true. In python the value of true is 1 and false is 0. When there is any number except 0 it returns true and false for zero.
Time complexity of this solution is greater then O(nlogn) but no extra space is required.
"""

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
arr.sort(key = bool, reverse = True)
print(arr)
