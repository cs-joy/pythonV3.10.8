''''

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”).
To add an item to the top of the stack, use `append()`. 
To retrieve an item from the top of the stack, use `pop()` without an explicit index.

'''

stack = [2, 4, 6, 8, 10]

# append() - add an item to the top of the stack
stack.append(12)
print(stack)
stack.append(14)
print(stack)


# pop() - retrieve an item from the top of the stack
stack.pop() # remove 14 # remove last element of the stack
print(stack)
stack.pop() # remove 12
print(stack)
stack.pop() # remove 10
print(stack)
