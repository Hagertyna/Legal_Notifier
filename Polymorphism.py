#Pholymorphism
class iamparrot:
    def canFly(self):
        print("Parrot can fly...")
    def canSwim(self):
        print("Parrot can't swim...")

class IamPenguin:
    def canFly(self):
        print("Penguin can't fly...")
    def canSwim(self):
        print("penguin can swim...")
# common interface
def flying_bird_test(bird):
     bird.canFly()
     bird.canSwim()
#Instantiate
#parrot class object
bird_par = iamparrot()

#penguin class object
bird_pen = IamPenguin()

#passing the object
flying_bird_test(bird_par)
print()
#call method
flying_bird_test(bird_pen)
