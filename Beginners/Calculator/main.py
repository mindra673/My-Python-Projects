import art
from replit import clear
def calculator():
  print(art.logo)
  #Add
  def add(a,b):
    return a+b
  
  #Subtract
  def subtract(a,b):
    return a-b
  
  #Multiply
  def multiply(a,b):
    return a*b
  
  #Divide
  def divide(a,b):
    return a/b
  
  operations= {'+':add, '-':subtract, '*':multiply, '/':divide}
  
  num1=float(input("What's the first number?:  "))
  num2=float(input("What's the second number?:  "))
  
  print("List of allowable operations:")
  
  for i in operations:
    print(i)
  
  operation_symbol=input("Which of the above operation do you want to perform?  ")
  
  answer=operations[operation_symbol](num1,num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  flag=input(f"Do you want to continue calculating with {answer}? Type 'y' for yes or else 'n' for Start over.\n")
  if flag=='y':
    should_continue=True
  else:
    clear()
    calculator()
  while should_continue:
    another_num=float(input("What's the next number?"))
    operation_symbol=input("Enter one of the above operations.")
    new_answer=operations[operation_symbol](answer,another_num)
    print(f"{answer} {operation_symbol} {another_num} = {new_answer}")
    answer=new_answer
    flag=input(f"Do you want to continue calculating with {new_answer}? Type 'y' for yes or else 'n' for Start over.\n")
    if flag=='y':
      should_continue=True
    else:
      clear()
      calculator()

calculator()
