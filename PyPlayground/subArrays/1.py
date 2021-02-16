a = [1, 2, 3, 4]
n = len(a)

# edge case


dp = [[0 for i in range(n+1)] for j in range(n)]
maxs = a[0]
for i in range(n):
    for j in range(i+1,n+1):
        dp[i][j] = dp[i][j-1] + a[j-1]
        if dp[i][j] > maxs: maxs = dp[i][j]

maxsss = sum([x for x in a if x >= 0])
if maxsss == 0: return max(arr)
print(maxs)
print(maxsss)


