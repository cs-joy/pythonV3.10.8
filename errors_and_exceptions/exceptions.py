
'''
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. 
Most exceptions are not handled by programs, however, and result in error messages as shown here:
'''

'''

10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

'''

num1 = 10
num2 = 0
# ZeroDivisionError
# print(num1/num2)

# NameError
# print(num1 * (spam+3))

# TypeError
# print('2' + num1)