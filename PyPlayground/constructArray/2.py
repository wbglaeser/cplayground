n = 5
k = 19
x = 1
M = 1000000007

res = {}
for i in range(1,k+1):
    if i == x:
        res.update({(i,n-1):1})
    else: res.update({(i,n-1):0})

for i in range(n-1):
    for j in range(k):
        pair = (j+1, n-i-2)
        res[pair] = 0

        for t in range(k):
            lp = (t+1, n-i-1)
            if pair[0] != lp[0]:
                res[pair] += (res[lp] % M)
print(res)
print(res[(1,0)])
