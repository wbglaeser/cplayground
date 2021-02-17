a = [1, 3, 1, 2]
n = len(a)
dp = [-1 for i in range(n-1)]
dp.append(a[-1])

for i in range(1,n):

    if a[n-1-i] < dp[n-i]:
        dp[n-1-i] = dp[n-i]
    else: dp[n-1-i] = a[n-1-i]

tp = 0
for i in range(n):
    if a[i] < dp[i]: tp += dp[i] - a[i]

print(dp)
print(tp)
"""
[-1,-1,-1,-1,-1,-1,2]
[-1,-1,-1,-1,-3,3,2]


[1,2,3,2,4]
[4,4,4,4,4]

[1,2,4,2,3]
[4,4,4,3,3]
"""
