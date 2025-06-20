for i in range(0,10):
    print(i)
    if(i>5):
        break



n =100
while(n>0):
    print(n)
    n=n//2
    if(n<50):
        break

for i in range(1,11):
    for j in range(2,10):
        print("{0}x{1}={2}".format(i,j,i*j))
        if(j>5):
            break


#continue
for i in range(0,10):
    if(i%2== 1):
        continue
    print(i)