

#tạo hàm basic
def xinchao():
    print("xin chào")

xinchao()

def chao(hovaten):
    print("xin chào :" + hovaten)
chao("phước")

#nhiều đối số, mỗi đối số cảnh nhau bởi dấu phẩy
def hi(ho,chulot,ten):
    print("xin chào : " + ho + chulot + ten)
print("phạm","thanh","phước")

# khi không xác định được 1 số đối số, chúng ta có thể sử dụng dấu *
def thoikhoabieu(*monhoc):
    for i in monhoc:
        print("môn" + monhoc[i])
    # print("Môn 1:" + monhoc[0])
    # print("Môn 2:" + monhoc[1])
thoikhoabieu("toan","ly","hoa")

































