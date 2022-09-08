# Multiple inheritance in Python

class Base1:
    def fun1(self):
        print("func1 of Base1 class is executing...")

class Base2:
    def fun2(self):
        print("func2 of Base2 class is executing...")

class Base3:
    def fun3(self):
        print("func3 of Base3 class is executing...")
        
class   MultiDer(Base1,Base2,Base3):
    def derFun(self):
        print("derfun of MultiDer class is executing...")

        
md1 = MultiDer()
md1.fun1()
md1.fun2()
md1.fun3()
md1.derFun()
