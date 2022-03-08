def numMax(a,b):
    if a > b:
        return a
    elif a == b:
        print(" a equals b...")

    else:
        return b
print("Maximum nuber between 10 and 30 is ", numMax(10,30))
print()

def hello(name , msg= "how are you?"):#func with default paramter
    print("Hello ",name , msg)
hello("Hagi","Have a nice day")
hello("Hagi")

#function with arbitrary arguments
def dimir(*args):
    sum= 0
    for i in args:
        sum += i
    return sum
print("sum of all integers between 1-7 is ", dimir(1,2,3,4,5,6,7))

def defaultArg(a,b,c=300):
#def defaultArg(a,40,300): we can use this technique to
#up on which b and c value is being 40 , 300 once func called
    print("a = {}, b ={}, c = {}..." .format(a,b,c))

defaultArg(10,20,30)
# ff outputs error missing c
#TypeError: defaultArg() missing 1 required positional argument: 'c'
defaultArg(5,7,300)
defaultArg(100,200)
#printed on declaration order
defaultArg(c= 100,b =200 ,a=1001)

defaultArg(a=100,c=200)