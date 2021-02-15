w = [2, 1, 1, 2, 1]
n = len(w)
dp = [0 for i in range(len(w)+1)]
print(dp)

fr = []
for i in range(1, n+1):
    lb = max(i-w[i-1], 1)
    rb = min(i+w[i-1], n) 
    fr.append((lb, rb))
    dp[i] = max(dp[i-1], rb)

print(dp)
print(fr)
res = [i for i in range(n+1)]
print(res)
rIndex = 0
for f in range(1, n+1):
    print(fr[f-1][0])
    print(f-fr[f-1][0])
    print(res[f-fr[f-1][0]]+1)
    res[f] = min(res[f], res[f-fr[f-1][0]]+1) 
    print("res: ", res)
    res[dp[f]] = min(res[f], res[dp[f]])
    print("res: ", res)

print(res[-1])
