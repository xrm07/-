N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Result=A
for i in range(M):
    Result.append(B[i])

Result.sort()
count=0
length=len(Result)-1
for i in range(length):
      if Result[i] in A :
        if Result[i+1] in A:
            count=1


if count>0:
    print("Yes")
else:
    print("No")