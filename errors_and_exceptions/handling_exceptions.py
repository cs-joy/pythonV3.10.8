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
'''

# ref: https://docs.python.org/3/tutorial/errors.html#syntax-errors

'''
Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.

When an exception occurs, it may have associated values, also known as the exception’s arguments. The presence and types of the arguments depend on the exception type.

The except clause may specify a variable after the exception name. The variable is bound to the exception instance which typically has an args attribute that stores the arguments.
For convenience, builtin exception types define __str__() to print all the arguments without explicitly accessing .args
'''

'''
try:
    raise Exception('spam', 'egg', 'args')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y, z = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    print('z =', z)
'''

'''
The exception’s __str__() output is printed as the last part (‘detail’) of the message for unhandled exceptions.

BaseException is the common base class of all exceptions. One of its subclasses, Exception, is the base class of all the non-fatal exceptions. Exceptions which are not subclasses of Exception are not typically handled, because they are used to indicate that the program should terminate. They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt the program.

Exception can be used as a wildcard that catches (almost) everything. However, it is good practice to be as specific as possible with the types of exceptions that we intend to handle, and to allow any unexpected exceptions to propagate on.

The most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):
'''

import sys

while True:
    try:
        
        print('1. exit')
        n = int(input())
        if n == 1:
            sys.exit()
        else:
            print('n is ', n)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")