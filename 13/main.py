a = input()
b = a.split()
cnt = 0
for i in b:
    if(i[0] == i[0].upper()):
        cnt = cnt + 1       
if(cnt == 2):
    print("YES")
else:
    print("NO")