# refff: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

'''
The `raise` statement allows the programmer to force a specified exception to occur. For example:
'''


# raise NameError('Hello There')

'''
The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses).
If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:
'''

# raise ValueError # shorthand for 'raise ValueError()'


'''
If you need to determine whether an exception was raised but don’t intend to handle it, 
a simpler form of the raise statement allows you to re-raise the exception:
'''

try:
    raise ValueError('Hello World')
except ValueError:
    print('An exception flew by!')
    raise
'''
An exception flew by!
Traceback (most recent call last):
  File "e:\GitHub\pythonV3.10.8\errors_and_exceptions\Raising_Exceptions.py", line 24, in <module>
    raise ValueError('Hello World')
ValueError: Hello World
'''