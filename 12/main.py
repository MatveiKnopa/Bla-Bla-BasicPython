a = int(input())
b = int(input())
for i in range(a,b+1,1):
    Flag = True
    if(i == 1):
        continue
    for g in range(2,i):
        if(i%g == 0):
            Flag=False
            break
    if(Flag):
        print(i)