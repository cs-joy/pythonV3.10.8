num = [ 2, 1, 3, 606, 4, 7, 6, 8, 404, 9, 43, 101, 5054, 34, 21, 501 ]


try:
  del num[6]
  print("deleted successfully!")
except:
  print("goes wrong")

for i in range(len(num)):
  print(num[i])
