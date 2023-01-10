
'''
If an unhandled exception occurs inside an except section,
it will have the exception being handled attached to it and included in the error message:
'''

try:
    open('database.txt')
except OSError:
    print('file not found')



















# https://docs.python.org/3/tutorial/errors.html#exception-chaining