a = [0,0,1,0]
N = len(a)

dp = [0] * N
for i in range(N):
    dp[i] = -1
 
# Traverse the array
for i in range(N):

    print(dp)
    idxLeft = max(i - a[i], 0)
    idxRight = min(i + (a[i] + 1), N)
    dp[idxLeft] = max(dp[idxLeft],
                        idxRight)

print(dp)
# Stores count of fountains
# needed to be activated
cntfount = 1
 
idxRight = dp[0]
 
# Stores index of next fountain
# that needed to be activated
idxNext = 0
 
# Traverse dp[] array
for i in range(N):
    idxNext = max(idxNext,
                  dp[i])
 
    # If left most fountain
    # cover all its range
    if (i == idxRight):
        cntfount += 1
        idxRight = idxNext
 
print(cntfount)
