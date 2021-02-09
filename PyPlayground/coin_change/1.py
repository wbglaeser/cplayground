W = 4
wt = [1, 2, 3]
n = len(wt)

dp = [[0 for i in range(W+1)] for i in range(n+1)]
print(dp)
for i in range(n):
    wi = wt[i]
    for w in range(W+1):
        
        if (i == 0) or (w == 0):
            dp[i][w] = 0

        if (wi <= w):
            dp[i][w] = dp[i][w-1] + wi

print(dp)

