n = 5
c = [1,2,3]
dp = [1] + [0 for i in range(n)]

for v in range(1, n+1):
    for i in range(len(c)):
        if c[i] <= v:
            dp[v] = dp[v-c[i]] + dp[v]
print(dp[-1])
