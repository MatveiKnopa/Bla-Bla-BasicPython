a = int(input())
for i in range(1,a+1,1):
    print(i,end="")

    for g in range(1,i+1):
        if(i%g == 0):
            print("+",end="")
    print()
