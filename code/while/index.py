n = -1
while(n<=0):
    n = int(input("nhập vào n: "))


i = 0
tong = 0
while(i<=n):
    tong+=i
    i+=1
print("tong =" , tong)


j=0
while(j<=10):
    print(j,"bên trong vòng lặp ")
    j+=1
    if(j>=5):
        break
else:
    print(j,"ngoài vòng lặp")