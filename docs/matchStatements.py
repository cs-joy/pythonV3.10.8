
def greet(a, b, operation):
  match operation:
    case "+":
      return a+b
    case "-":
      return a-b
    case "*":
      return a*b
    case "/":
      return a/b
    case "%":
      return a%b
    case _:
      return "invalid oprator"

num1 = 4
num2 = 2
operator = "-"
greet(num1, num2, "-")
