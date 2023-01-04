'''

It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports); 
note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.
'''

'''
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
'''

'''

The try statement works as follows.

     First, the try clause (the statement(s) between the try and except keywords) is executed.

     If no exception occurs, the except clause is skipped and execution of the try statement is finished.

     If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

     If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. 
An except clause may name multiple exceptions as a parenthesized tuple, for example

```
... except (RuntimeError, TypeError, NameError):
...     pass
```

'''



'''
A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class). 
For example, the following code will print B, C, D in that order:
'''

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# ref: https://docs.python.org/3/tutorial/errors.html#syntax-errors