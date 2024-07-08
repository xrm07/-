N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Result=A+B
Result.sort()
count=0
length=len(Result)-1
for i in range(length):
  print(Result[i],Result[i+1])
  if Result[i]==Result[i+1]:
      print(Result[i])
      if Result[i] in A :
        count=1


if count>0:
    print("Yes")
else:
    print("No")