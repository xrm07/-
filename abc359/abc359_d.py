N,K=map(int,input().split())
S=input()
s=[]
i=0
while i+K<N:
    ss=s[i:i+K]
    s.append(ss)

l=len(s)
s=l-K+1
last=[]
count=0
for i in range(len(s)):
    for j in range(K):
        if s[i][j]!=s[i][j+1]:
            j+=1
            last.append(s[i])
        else:
            break

goal=count/K
print(goal)
    

