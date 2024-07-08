from random import random


N,K=map(int,input().split())
A=list(map(int,input().split()))
A_a=A
c=0
do=[]
for i in range(N):
    while c<K:
        j=random.randint(0,N-1)
        A.pop(j)
        c+=1
        do.append(j)