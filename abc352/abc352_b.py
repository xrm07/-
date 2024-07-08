S=input()
T=input()
count=0
L=[]
for i in range(len(S)):
    for j in range(len(T)):
        if S[i]==T[j]:
            number=j+1
            L.append(number)
            break

print(*L)

