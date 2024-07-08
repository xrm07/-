count=0
N=int(input())
A=list(map(int,input().split()))
for i in range(N-1):
  if count==0:
    if A[0]<A[i+1]:
        count=i+2
        break

if count==0:
    print("-1")
else:
    print(count)
    