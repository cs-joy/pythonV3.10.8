# s: https://www.youtube.com/watch?v=rfscVS0vtbw&t=10032s

# 2d list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0]) # out/ 1

print(number_grid[2][1]) # out/ 8


# nested loop

for row in number_grid:
    print(row)

    # out::
    """
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    [0]
    """
    # i want to access each of these individual attributes inside of each of these array elements

for row in number_grid:
    for col in row:
        print(col)