class simpleClass2:
    # constructor
    def __init__(self):
        self.name="tung"
    
    #methods
    def hello(self):
        print("hello " + self.name)
    #static methods
    @staticmethod
    def hi(name):
        print("hi " + name)
objectC = simpleClass2()
objectD = simpleClass2()


objectC.hello()
objectD.hi("peter")

# simpleClass2.hello()
simpleClass2.hi(name="phước")
# phân biệt methods và static methods