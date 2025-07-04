# open()
# "x" - tạo file
try:
    f = open("vidu1.txt","x")
except Exception as a:
    print(a)
finally:
    f.close()


# "w" - ghi dữ liệu file
# "a" - nối vào file
try:
    with open("vidu1.txt","w") as f:
        f.write("xin chào các bạn")
        f.close()
except Exception as a:
    print(a)

try:
    with open("vidu1.txt","a") as f:
        f.write("xin chào các bạn")
        f.close()
except Exception as a:
    print(a)

# "r" - đọc file
try:
    with open("vidu1.txt","r") as f:
        list_noidung = f.read()
        i=1
        for noidung in list_noidung:
            print(str(i) + " : " + noidung)
            i+=1
        print(list_noidung)
except Exception as a:
    print(a)
        





