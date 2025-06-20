import math

xA = float(input("Nhập vào xA: "))
yA = float(input("Nhập vào yA: "))
xB = float(input("Nhập vào xB: "))
yB = float(input("Nhập vào yB: "))
xC = float(input("Nhập vào xC: "))
yC = float(input("Nhập vào yC: "))

ab = math.sqrt((xB-xA)**2 + (yB-yA)**2)
bc = math.sqrt((xC-xB)**2 + (yC-yB)**2)
ac = math.sqrt((xC-xA)**2 + (yC-yA)**2)

if(ab+bc >ac) and (ab+ac> bc) and (bc+ac>ab):
    cv = ab+ac+bc
    print("chu vi =",cv)
    p =cv/2
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("diện tích = ",s)
else:
    print("không tạo thành tam giác")