#for index

for i in range(10):
    print(i)
n = int(input("nhập n : "))
tong = 0
for i in range(n+1):
    tong+=i
print("tổng =",tong)


# vòng lặp for, có bước tăng tùy chỉnh

for i in range(0,11,2):
    print(i)
for i in range(11,0,-2):
    print(i)


# vòng lặp for duyệt các phần tử của list
colors = ["red","green","black"]
for color in colors:
    print(color)

#vòng lặp for diệt phần tử theo vị trí
for i in range(len(colors)):
    print(colors[i])
 