print("chọn chức năng")
print("1 . thêm từ vựng")
print("2 . tra cứu ")
print("3 . cập nhật từ vựng")
print("4 . Xóa 1 từ vựng")
print("5 . Xóa all từ vựng")
print("6 . in toàn bộ từ vựng")
print("7 . in all từ vựng : nghĩa")
print("8 . kết thúc chương trình")

tudien = {} 
while(True):
    luachon = int(input("nhập vào lựa chọn của bạn : "))
    if(luachon == 1 or luachon == 3):
        tuvung = input("nhập từ vựng ")
        ynghia = input("nhập ý nghĩa ")
        tudien[tuvung]=ynghia
    elif(luachon == 2):  
        tuvung = input("nhập từ vựng ")
        print("ý nghĩa",tudien[tuvung])
    elif(luachon == 4):
        tuvung = input("nhập từ vựng cần xóa ")
        tudien.pop(tuvung)
        print("đã xóa từ vựng")
    elif(luachon == 5):
        tudien.clear()
        print("đã xóa all từ vựng")
    elif(luachon == 6):
        print("in toàn bộ từ vựng")
        for x in tudien.keys():
            print(x)
    elif(luachon == 7):
        print("in all từ vựng : nghĩa") 
        for x,y in tudien.items():
            print(x , ":" , y)
    elif(luachon == 8): 
        break
    else:
        print("nhập lựa chọn không đúng")