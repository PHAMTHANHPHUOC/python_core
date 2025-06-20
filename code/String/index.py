#chuỗi nhiều dòng
chuoi_nhieu_dong = '''
Dòng 1
Dòng 2
Dòng 3
'''
print(chuoi_nhieu_dong)


# kiểm tra chuỗi có thuộc chuỗi khác
chuoi_1 ="phước Đẹp"
chuoi_2 ="Đẹp"
chuoi_3 ="trai"

if chuoi_2 in chuoi_1:
    print("chuỗi 2 là chuỗi của 1")
else:
    print("chuỗi 2 không là chuỗi con  của chuỗi 1")

if chuoi_3 in chuoi_1:
    print("chuỗi 3 là chuỗi của 1")
else:
    print("chuỗi 3 không là chuỗi con  của chuỗi 1")
    
# viết hoa chữ đầu của chuỗi
s= "hôm nay trời đẹp quá!"
s= str.capitalize(s)
print(s)

#viết hoa toàn bộ chuỗi
s= s.upper()
print(s)

#viết thường toàn bộ chuỗi
s= s.lower()
print(s)

#đếm số lượng chuỗi con
s="lập trình python. bạn nên học python"
print(s.find("python"))# trả về -1 nếu không tìm thấy

#đếm bao nhiêu chuỗi
print(s.count("python"))

#thay thế chuỗi
s="lập trình python. bạn nên học python"
s= s.replace("python","PYTHON")
print(s)

# cắt chuỗi thành một LIST
s="lập trình python. bạn nên học python"
list1 = s.split(" ")
print(list1)

#format
print("{0}+{1}={2}".format(1,2,1+2))

#lấy chuỗi con
print(s[0:10])