#                                                 **NOTE ON RECURSION**
Recursive function: A recursive function calls itself. This mean that a new function is called from within the original function.

For example look at the code below and assume a linked list counting from 0 to n by 1.

```python
def print_list(head):
    if head is not None:
        print(head.data)
        print_list(head.next)
```

The first function looks at the head of the list and prints it. It then creates a new function to print the next element. However,
first function hasn't ended yet. It can't end until all the functions within it end. This is key to understanding.

If we look at the call stack (the list of running functions) it looks like this:

```python
print_list() # the original outer most function, waiting for internal functions to end.
    print_list() # the new function called within the original func.
```

This just keeps on going. The new function calls another function. Now our stack looks like this:

```python
print_list() # the original function
    print_list() # level 1 function.
    	print_list() # level 2 function.
```

The call stack keeps getting bigger and bigger because none of the outer functions can terminate because they are waiting on inner
functions.

```python
print_list() # the original function
    print_list() # level 1 function.
    	print_list() # level 2 function.
            ...
                ...
                    ...
                        print_list() # level 1000 - Recursion depth hit. Program ends and error displayed.
```

The call stack keeps getting bigger and bigger because none of the outer functions can terminate because they are waiting on inner
functions.

Recursion depth is a count of how many layers are active inside your recursive function. The default recursion depth limit for 
Python 3 is 1000. The limit exists to prevent a stack overflow caused by too much (possibly infinite) recursion.
Recursion is a cool tool and you should use it (or at least understand it). However, some languages have optimized tail call 
recursion (what is the kind of recursion being shown above) and avoid this problem by ending the outer function when the inner one is called. Python has not.

If you are writing a function that may hit the recursion limit it may be better to approach it iteratively (at least in Python).

© 2022 GitHub, Inc.
Terms
Privacy
