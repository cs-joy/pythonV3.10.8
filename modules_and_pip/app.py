# modules - a modules is essentially just a python file that we can import to our current python file
# Python Module:: https://docs.python.org/3.10/py-modindex.html

# user defined modules
import useful_tools

# built in modules
import base64

print(useful_tools.roll_dice(10))

encoded = base64.b64encode(b'hello world')
print(encoded)

data = base64.b64decode(encoded)
print(data)