n = 11
coins = [1,2,5]
dp = [n+1 for i in range(n+1)]

for i in range(n+1):
    for c in coins:
        if c <= i: dp[i] = min(dp[i-c]+1, dp[i])
    if dp[i] == n+1: dp[i] = 0

print(dp)
print(dp[n])
