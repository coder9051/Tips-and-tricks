# Binary Search
Searching is the process of finding some particular element in the list. If the element is present in the list, then the process is called successful, and the process returns the location of that element. Binary search follows the divide and conquer approach in which the list is divided into two halves, and the item is compared with the middle element of the list. If the match is found then, the location of the middle element is returned. Otherwise, we search into either of the halves depending upon the result produced through the match.

## Note 
Binary search is the search technique that works efficiently on sorted lists. Hence, to search an element into some list using the binary search technique, we must ensure that the list is sorted.

## Algorithm
1. The starting element is called ‘low’ and the final element is called ‘high’. Using these values we try to narrow down the middle element by using the formula (low+high)//2. This operation basically performs a floor function to achieve the desired middle element.
2. The next step is to check if the value of the middle element is equivalent to the desired value. If yes, then the search is successful and can be terminated.
3. If the desired value is lesser than the middle element, all the values from the middle element to the ‘high’ value are eliminated. And the repetition of step 2 and 3 takes place.
4. If the desired value is greater than the middle element, all the values from the middle element to the ‘low’ value are eliminated. And the repetition of step 2 and 3 takes place.

## Python Code

```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
  
arr = [ 2, 3, 4, 10, 40 ]
x = int(input("Enter number which you want to search: "))
 
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
```
## Time Complexity
 **Best Case Complexity**  - In Binary search, best case occurs when the element to search is found in first comparison, i.e., when the first middle element itself is the element to be searched. The best-case time complexity of Binary search is O(1).

 **Average Case Complexity** - The average case time complexity of Binary search is O(logn).

 **Worst Case Complexity** - In Binary search, the worst case occurs, when we have to keep reducing the search space till it has only one element. The worst-case time complexity of Binary search is O(logn).
 
 ## Space Complexity
 The space complexity of binary search is O(1).
 
 ## Conclusion
 The major limitation of binary search is that there is a need for the sorted array to perform the binary search operation. If the array is not sorted the output is either not correct or maybe after a long number of steps and according to the data structure, the output should come in a minimum number of steps.
