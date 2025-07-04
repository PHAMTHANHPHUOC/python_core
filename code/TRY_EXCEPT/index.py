# try:
#     #đoạn này dữ đoán lỗi
# except:
#     #hoạt động khi xãy ra lỗi
# else:
#     #thực thi đoạn này nếu như không có lỗi
# finally:
#     #cho phép bạn thực thi mã, bất kể kết quả của các khối try có bị lỗi hay không




try:
    a = int(input("nhập vào số nguyên a :"))
    print(str(a) + " + 5 = " + str(a+5))
except Exception as e:
    print("nhập dữ liệu không chính xác" , e)
else:
    print("không có lỗi xãy ra")
finally:
    print("kết thúc chương trình")