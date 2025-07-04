# bài tập về động vật

# xây dựng class "cha" (base class) :
class Animal:
    #constructor : xây dựng ra đối tượng
    def __init__(self,animalTypeA,nameA,widthA,hieghtA,weightA):
        self.animalType = animalTypeA
        self.name   = nameA
        self.width  = widthA
        self.hieght = hieghtA
        self.weight = weightA
    #phát ra âm thanh:
    def makeVoice(self):
        print("unknow voice")
    
    #in thông tin
    def printMe(self):
        print("animalType={0},name={1},width={2},height={3},weight={4}".format(self.animalType,self.width,self.hieght,self.weight))
a1 = Animal("con người","Phước"," ","165cm","60kg")
a1.printMe()
a1.makeVoice()


class Dog(Animal):
    #constructor của lớp con:
    def __init__(self,nameA,widthA,hieghtA,isChampionA):
        #gọi constructor của lớp cha
        Animal.__init__(self,"dog",nameA,widthA,hieghtA,weightA)
        # gán giá trị cho các thuộc tính bổ sung
        self.isChampion = isChampionA

    # override method
    def makeVoice(self):
        print("{0}: gâu gâu".format(self.name))
dog1 = Dog("cậu vàng","80cm","40cm","20kg",True)
dog2 = Dog("Mật","820cm","420cm","220kg",True)
dog1.makeVoice()
dog1.printMe()
dog2.makeVoice()
dog2.printMe()
