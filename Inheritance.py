# Creatingclass and object in python
class myBird:
  def __init__(self):
    print("myBird class constructor is executing...")
  def whatType(self):
    print("I am a Bird...")
  def canSwim(self):
    print("I can Swim...")


# pengiun class inheriting the attributes of from Bird class
class iamPenguin(myBird):
    def __init__(self):
        super().__init__()
        print("iamPenguin class constructor is executing...")
    def whoisThis(self):
        print("I am penguin")
    def canRun(self):
        print("I can run faster...")

# Accessing the child class's attributes(Inheritance)
pg1 = iamPenguin()
pg1.whatType()   # defined in myBird class
pg1.whoisThis()  # defined in iamPenguin class
pg1.canSwim()    # defined in myBird class
pg1.canRun()     # defined in iamPengui 