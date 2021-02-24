

def cal(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  
val = cal(1, 2, '+')
print(val)