S=input()
T=input()
L=[-1]

n=len(S)
m=len(T)

#abc352_remake

for i in range(n):
    for j in range(L[-1]+1,m):
        if S[i]==T[j]:
            L.append(j)
            break

#abc352_teacher's answer

while i<n:
    while j<m and S[i]!=T[j]:
        j+=1
    print(j)
    j+=1
    i+=1



