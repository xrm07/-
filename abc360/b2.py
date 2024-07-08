S,T=map(str,input().split())
n=len(S)
f=0
ans=[]
t=""
for i in range(1,len(S)):
  ans=[]
  for j in range(0,len(S)//i,i):
    ans.append(S[j:j+i])
    print(ans)
  for j in range(len(ans)):
    for k in range(len(S)//i):
        p=ans[j][k]
        t+=p
    if T in t:
        f=1
        t=""

if f==1:
    print("Yes")
else:
    print("No")