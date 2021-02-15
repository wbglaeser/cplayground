n = 10
c = [2,5,3,6]
dp = [1] + [0 for i in range(n)]

for i in range(len(c)):
    for v in range(1, n+1):
        if c[i] <= v:
            dp[v] = dp[v-c[i]] + dp[v]
print(dp[-1])
