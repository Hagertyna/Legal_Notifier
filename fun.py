def mul(x,y):
  return x *y
#using multiple arguments
def new_names(name1, name2, name3):
    print("The first name is " + name1)
    print("The second name is " + name2)
    print("The last name is " + name3)
    
new_names(name1 = "Hagi", name2 = "Yeye", name3 = "daye")
#defining function degree
def degrees(x):
    return 15 * x

print(degrees(2))
print(degrees(3))

def fruits(name):
    for i in name:
        print(i)

fruit_names = ["Apple", "banana", "watermelon"]
fruits(fruit_names)
