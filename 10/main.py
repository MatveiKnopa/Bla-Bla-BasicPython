a = int(input())
for i in range(1,a//2+2,1):
    for g in range(i):
        print("*",end="")
    print()
for i in range(a//2,0,-1):
    for g in range(i):
        print("*",end="")
    print()