#tạo mới set
monhoc = {"toán","lý","hóa"}
print(monhoc)

#duyệt các phần tử bên trong 

for x in monhoc:
    print(x)

#thêm phần tử
monhoc.add("lịch sử")
print(monhoc)

#thêm nhiều phần tử
hocthem = {"anh văn", "nhạc"}
monhoc.update(hocthem)
print(monhoc)

#thêm list và set
hocphudao = ["võ thuật","dance"]
print(hocphudao)

monhoc.update(hocphudao)
print(monhoc)

#xóa
monhoc.remove("dance")
monhoc.discard("toán")#nếu không tồn tại thì thôi

print(monhoc)

monhoc.pop()# xóa phần tử đầu tiên
print(monhoc)

monhoc.clear()
print(monhoc)