##                                     **Duplicate element in a limited range array**
Q. Given a limited range array of size n cotaining elements between 1 and n-1 with one element repeating, find the duplicate number
in it without using any extra space.
We are given an array arr[] of size n. Numbers are from 1 to (n-1) in random order. The array has only one repetitive element. We need to find the repetitive element.

# SOLUTION 1: 
We know sum of first n-1 natural numbers is (n – 1)*n/2. We compute sum of array elements and subtract natural number sum from it to find the only missing element.

Time complexity : O(n)

Auxillary space : O(1)

```python
arr = [1, 4, 2, 3, 4, 5]
n = len(arr) - 1 #It is also equal to max of list.
sumArr = sum(arr)
originalSum = (n*(n+1))//2
repeatingElement = sumArr - originalSum
print(repeatingElement)
```

# SOLUTION 2: 
Use a hash table to store elements visited. If a seen element appears again, we return it.

Time complexity : O(n)

Auxillary space : O(n)

```python
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
```

# SOLUTION 3: 
The idea is based on the fact that x ^ x = 0 and x ^ y = y ^ x.
*   Compute XOR of elements from 1 to n-1.
  
*   Compute XOR of array elements.
 
*   XOR of above two would be our result.
 
Time complexity : O(n)

Auxillari space : O(1)

```python
def findRepeating(arr, n):
     
    res = 0
    for i in range(0, n-1):
        res = res ^ (i+1) ^ arr[i]
    res = res ^ arr[n-1]
         
    return res

arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
n = len(arr)
print(findRepeating(arr, n))
```

# SOLUTION 4: 
We can solve this problem in constant space. Since the array contains all distinct elements except one and all elements lie in range 1 to n-1, we can check for a duplicate element by marking array elements as negative using the array index as a key. For each array element nums[i], invert the sign of the element present at index nums[i]. Finally, traverse the array once again, and if a positive number is found at index i, then the duplicate element is i.

The above approach takes two traversals of the array. We can achieve the same in only a single traversal. For each array element nums[i], invert the sign of the element present at index nums[i] if it is positive; otherwise, if the element is already negative, then it is a duplicate.

Time complexity : O(n)

Auxillary space : O(0)

```python
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
```
