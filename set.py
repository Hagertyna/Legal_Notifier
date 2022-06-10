newset = {True, "Python", 5, 3.7}
print(newset)

#lets prnit as a set 

fruits_set = set(("banana", "apple", "fig"))
print(fruits_set)
# each on new line
for x in fruits_set:
    print(x)
# the output will be boolean whch is True
print("apple" in fruits_set)
# add new frut
fruits_set.add("orange")
print(fruits_set)
