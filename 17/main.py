a = int(input())
b = input()
c = ""
lst = list(b)
for i in range(0,10,1):
    lst.append(str( i))
import random
random.shuffle(lst)
for j in range(10):
    c = ""
    for i in range(a):
        num = random.randint(0,len(lst)-1)
        c = c + lst[num]
    print(c)
 
