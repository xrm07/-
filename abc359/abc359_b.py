N=int(input())
A=list(map(int,input().split()))
#Aの要素は２N個
i=0
count=0
N=N*2

while i+2<N:
  if A[i]==A[i+1]:
    break
  else:
    if A[i]==A[i+2]:
      count+=1
      i+=1
    else:
      i+=1

print(count)