#fun with return statement 
def selam():
    print("Hello! I LOVE to code in python.")

def selam2():
    #document string
    '''
    This is 
    a multi line
    text
    '''
    #returns back the control to the caller 
    #mainly used to return a value to the caller of the function
    return "Hello! I  love to code in Python."
selam()
#ff outputs nothing
selam2()

# we should call it inside print() function
print(selam2())
print(selam2.__doc__)