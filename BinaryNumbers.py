import sys


n = int(input().strip())
b = str("{0:b}".format(n))
count = 0 
aux = 0
for i in range(len(b)):

    if b[i] == "1":
        count = count + 1
    else:
        if aux <= count:
            aux = count 
            count = 0
        else:
            count = 0

    if count > aux:
        aux = count
            
print(aux)
