H=int(input())
Height=0
i=0
count=0
while True:
    Height+=2**i
    i+=1
    count+=1
    if (Height>H):
        break
    else:
        continue

print(count)