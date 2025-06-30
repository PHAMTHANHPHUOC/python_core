# lưu key và value

#vd
sinhvien = {
    "NAME" :"PHẠM THANH PHƯỚC",
    "LOP"  :"TPM7"
}
print(sinhvien["NAME"])
print(sinhvien)

# sử dụng get() để lấy giá trị
print(sinhvien.get("LOP"))

# Cập nhật giá trị
sinhvien["LOP"]= "httd"
print(sinhvien)
sinhvien.update({"NAME" : "phước","LOP" : "mmn"})#nhiều giá trị
print(sinhvien)

# thêm cặp key:value

sinhvien["NAMHOC"] = 2025
print(sinhvien)

sinhvien.update({
    "NOISINH" : "TRAVINH"
})
print(sinhvien)

#xóa đi cột mục

sinhvien.pop("NOISINH")
print(sinhvien)
sinhvien.popitem()#xóa đi cặp key:value cuối cùng
print(sinhvien)
del sinhvien["LOP"]
print(sinhvien)

#XÓA ALL CLEAR
sinhvien.clear()
print(sinhvien)

#in all các tên khóa trong từ điển
for x in sinhvien:
    print(x)

#duyệt các giá trị    
for x in sinhvien.values():
    print(x)
#duyệt các từ khóa   
for x in sinhvien.keys():
    print(x)
#duyệt các cặp khóa =  giá trị  
for x,y in sinhvien.items():
    print(x,y)