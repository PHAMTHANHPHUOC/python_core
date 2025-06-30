import math
print("giải phương trình ax^2+bx+c=0")
a = float(input("nhập a :"))
b = float(input("nhập b :"))
c = float(input("nhập c :"))

print("{0}x^2+{1}x+{2}=0".format(a,b,c))

if(a!=0):
    delta = b**2-4*a*c
    if(delta<0):
        print("ptvn")
    elif(delta==0):
        x=-b/(2*a)
        print("pt co nghiem kep x1=x2",x)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("co nghiem kep x1={0} va x2={1}".format(x1,x2))

else:
    print("không phải phương trình bậc 2")    
