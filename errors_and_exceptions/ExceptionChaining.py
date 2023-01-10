
'''
If an unhandled exception occurs inside an except section,
it will have the exception being handled attached to it and included in the error message:
'''

'''
try:
    open('database.txt')
except OSError:
    raise RuntimeError('Unable to handle error')
'''

'''
Traceback (most recent call last):
  File "e:\GitHub\pythonV3.10.8\errors_and_exceptions\ExceptionChaining.py", line 8, in <module>
    open('database.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'database.txt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "e:\GitHub\pythonV3.10.8\errors_and_exceptions\ExceptionChaining.py", line 10, in <module>
    raise RuntimeError('Unable to handle error')
RuntimeError: Unable to handle error
'''



'''
To indicate that an exception is a direct consequence of another, the `raise` statement allows an optional `from` clause:
......................
# exc must be exception instance or None.
raise RuntimeError from exc
'''

'''
This can be useful when you are transforming exceptions. For example:
'''

'''
def func():
    raise ConnectionError


try:
    func()

except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
'''

'''
Traceback (most recent call last):
  File "e:\GitHub\pythonV3.10.8\errors_and_exceptions\ExceptionChaining.py", line 46, in <module>
    func()
  File "e:\GitHub\pythonV3.10.8\errors_and_exceptions\ExceptionChaining.py", line 42, in func
    raise ConnectionError
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "e:\GitHub\pythonV3.10.8\errors_and_exceptions\ExceptionChaining.py", line 49, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
'''



'''
It also allows disabling automatic exception chaining using the from None idiom:
'''

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

# For more information about chaining mechanics, see Built-in Exceptions(https://docs.python.org/3/library/exceptions.html#bltin-exceptions).








# https://docs.python.org/3/tutorial/errors.html#exception-chaining