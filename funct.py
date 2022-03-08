def Add(x,y):
    print("Adition operation...")
    return (x+y)
def Multply(x,y):
    print("Multition operation...")
    return (x*y)
def Subtract(x,y):
    print("Substraction operation...")
    return (x-y)
def devide(x,y):
    print("division operation...")
    return (x/y)
def Selection():

    print("Main Menu...")
    print(" 1 > Add two numbers...")

    print(" 2 > Multiply two numbers...")
    print(" 3 > Substract two numbers...")
    print(" 4 > Divide two numbers...")
    ch = int(input("Please select your option number..."))
    return ch
def calculation():
    ch = Selection()
    num1 = int(input("Type first number..."))
    num2 = int(input("Please enter second number..."))

    if ch == 1:
        result =Add(num1,num2)
        print(result)
    elif ch==2:
          result =Multply(num1,num2)
          print(result)
    
    elif ch==3:
          result =Subtract(num1,num2)
          print(result)
    elif ch==4:
          result =devide(num1,num2)
          print(result)
    else:
        print("done calculation!")
calculation()