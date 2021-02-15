n = 4
k = 3
x = 1

def sumOpts(n, k, x, pval=None, idx=0):
    count = 0

    if idx == 0:
        for j in range(2,k+1):
            count += sumOpts(n, k, x, pval=j, idx=idx+1)

    if idx == n-3:
        if pval == x: return k-1
        else: return k-2

    if (idx > 0) and (idx < n-3):
        for j in range(1, k+1):
            if j != pval:
                count += sumOpts(n, k, x, pval=j, idx=idx+1)

    return count

print(sumOpts(n,k,x))

