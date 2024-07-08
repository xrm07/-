N,K=map(int,input().split())
A=list(map(int,input().split()))
count=1
new_K=K
#print(new_K)
for i in range(N):
    if K>=A[i]:
      K-=A[i]
    else:
      K=new_K-A[i]
     # print(K)
      count+=1

#for i in range(10):
#  print(i)

print(count)
    
    
    









#K-=N[i]
#    if K<N[i+1]:
#        count+=1
#        break
 #   elif K>=N[i+1]:
  #      K-=N[i+1]
    #     count+=1
     #    if K==0: