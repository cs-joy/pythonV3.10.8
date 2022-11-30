# exponent function
# # how to build exponent function?
# An exponent function is basically gonna allow us to take a certain number and raise it to a specific power

print(2 ** 3) # 2^3

# going to build exponent function
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))

# thus the basics of build power function/ exponent function