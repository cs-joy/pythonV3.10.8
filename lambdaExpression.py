def make_incrementor(num):
    return lambda n: n + num

f = make_incrementor(22)
print(f(0)) # 22

print(f(11)) # 33

print(f(5)) # 27
