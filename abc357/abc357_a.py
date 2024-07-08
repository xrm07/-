# Description: AtCoder Beginner Contest 357 A問題
count=0
N,M = map(int, input().split()) 
H=list(map(int,input().split()))
for i in range(N):
    if M<0:
        break
    elif M<H[i]:
        break
    elif M>=H[i]:
        M-=H[i]
        count+=1

print(count)

    