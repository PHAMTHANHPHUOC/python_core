# doi so thap phan qua nhi phan
n = -1
while(n<=0):
    n = int(input(" nhap so n > 0 :" ))
x=n
ketqua = ""
while(n>0):
    ketqua = str(n%2) + ketqua
    n=n//2
print(" so nhi phan cua ", x,"la ", ketqua)