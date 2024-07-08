S=str(input())
for i in range(3):
    if S[i]=="R" :
        f=0
        break
    elif S[i]=="M":
        f=1
        break

if f==0:
    print("Yes")
else:
    print("No")
