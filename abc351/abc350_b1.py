N=int(input())
count=0
A=list(input())
while count<N:
    a = list(input())
    A+=a
    N+=1

count=0
B=input()
while count<N:
    b=list(input())
    B+=b
    count+=1
    
for i in range(len(A)):
    if A[i]==B[i]:
        h=i/N
        w=i//N
    
print(h+1,w+1)