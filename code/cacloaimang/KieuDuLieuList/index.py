#list rỗng
emtylist = []

# tạo ra một đối tượng list
emtylist2 = list()

print(emtylist)
print(emtylist2)

#Tạo list có dữ liệu
colors = ["red","green","blue","orange"]
print(colors)

#lấy ra 0->2-1
print(colors[0:2])

print(colors[1])
#thêm phần tử vào cuối list
colors.append("grey")
print(colors)
colors[len(colors):]= ["violet"]#c2


#chèn
colors.insert(2,"black")
print(colors)

#số lượng phần tử có trong list
print("số lượng màu :",len(colors))

#đếm số lượng phần tử thỏa điều kiện
print("đếm ngọc",colors.count("black"))

#Xóa phần tử ra khỏi list
colors.remove(colors[0])
colors.remove("black")
print(colors)

#kiểm tra phần tử có bên trong list: in
if("blue" in colors):
    colors.remove("blue")
    print(colors)
#xóa khỏi list bằng vị trí
colors.pop(0)
print(colors)

#đảo ngược list
colors.reverse()
print(colors)

#sắp xếp tăng dần
colors.sort()
print(colors)

#sắp xếp ngược theo thứ tự
colors.sort(reverse=True)
print(colors)

#xóa sạch danh sách trong list
colors.clear()
print(colors)