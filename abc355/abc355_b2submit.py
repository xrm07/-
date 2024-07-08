N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Result=[]
for i in range(N):
   Result.append(A[i])

for i in range(M):
   Result.append(B[i])

Result.sort()

#print(Result)
count=0
length=N+M-1

for i in range(length):
  for j in range(len(A)-1):
    if Result[i] in A:
      #print(Result[i],A[j])
      if Result[i+1] in A:
        count=1


if count>0:
    print("Yes")
else:
    print("No")