# return - the return keyword can basically allow python to return information from a function


def cube(num):
    return num*num*num

print(cube(3))

# with variable
result = cube(4)
print("result= " + str(result))

def after_return(n):
    return n*n
    print("something") #does not printed out

print(after_return(2))