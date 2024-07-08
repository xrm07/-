S, T = map(str, input().split())
n = len(S)
f = 0
ans = []
t = ""
for i in range(1, len(S)):
    ans = []
    for j in range(0, len(S), i):
        ans.append(S[j:i + j])
    for k in range(len(S) // i):
        for j in range(len(ans)):
            try:
                p = ans[j][k]
                t += p
            except:
                IndexError
                continue
        if T == t:
           f = 1
    t = ""

if f == 1:
    print("Yes")
else:
    print("No")