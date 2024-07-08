#N=list(map(int,input().split()))
#M=[input().split() for _ in range(2)]

#print(N)
#print(M)

N=int(input())
S=[input() for i in range(N)]
count=0
for i in range(N):
    if S[i]=="Takahashi":
        count+=1

print(count)



