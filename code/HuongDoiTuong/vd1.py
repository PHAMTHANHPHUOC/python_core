# Ví dụ về class đơn giản
class simpleClass:
    # attribute
    i=5
    #__init__
    def __init__(self):
        self.j = 7
    #method:
    def printMe(self):
        print(self.j)
    
objectA = simpleClass()
objectB = simpleClass()

objectA.printMe()
print(objectB.i)

# thay đổi giá trị của thuộc tính
objectA.i = 100
objectB.j = 500
print(objectA.i)
objectB.printMe()

# thử truy cập phương thức không phải static 
# simpleClass.printMe()