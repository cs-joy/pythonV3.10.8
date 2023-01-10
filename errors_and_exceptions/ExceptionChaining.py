
'''
If an unhandled exception occurs inside an except section,
it will have the exception being handled attached to it and included in the error message:
'''

try:
    open('database.txt')
except OSError:
    raise RuntimeError('Unable to handle error')

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


















# https://docs.python.org/3/tutorial/errors.html#exception-chaining