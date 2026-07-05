a = int(input())
b = int(input())
c = 0
for i in range(a,b):
    i = i ** 3
    if(str(i)[-1]=="4" or str(i)[-1]=="9"):
        c = c + 1
print(c)