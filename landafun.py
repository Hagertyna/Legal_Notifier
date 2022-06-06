
# Lambda with user function
def multiply(n):
    return lambda x: x * n

double = multiply(2)
triple = multiply(3)

print(double(10))
print(triple(10))
