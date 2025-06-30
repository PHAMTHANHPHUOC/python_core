import random

thungphieu = set()
sodienthoai = {}
while(True):
    print("----------------MENU-------------")
    print("vui lòng chọn chức năng")
    print("1- thêm 1 số điện thoại vào thùng phiếu thưởng")
    print("2- xóa 1 số điện thoại vào thùng phiếu thưởng")
    print("3- Quay số ngẫu nhiên lấy ra 1 số đt trúng thưởng")
    print("4- kết thúc chương trình")
    print("thùng phiếu hiện tại")

    luachon = int(input("lựa chọn: "))
    print(thungphieu)


    if(luachon == 1):
        sodienthoai = input("nhập số điện thoại dự thưởng")
        thungphieu.add(sodienthoai)
    elif(luachon == 2):
        sodienthoai = input("nhập số điện  cần xóa")
        thungphieu.discard(sodienthoai)
    elif(luachon == 3):
        
        index =random.randint(0,len(thungphieu))
        i = 0 
        print("vị trí trúng thưởng " + str(index)) 
        for x in thungphieu:
            if(i == index):
                print("chúc mừng"+ x + "trúng thưởng")
                thungphieu.discard(x)
            i = i + 1
    else:
        break
    x = input("nhập phím bất kỳ để tiếp tục")