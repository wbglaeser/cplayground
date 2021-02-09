def gt(n,m, memo={}):

    # base cases
    if n == 0 or m == 0: return 0
    if n == 1 or m == 1: return 1
    
    # memo lookup
    if (n,m) in memo: return memo[(n,m)]

    memo[(n,m)] = gt(n-1, m, memo) + gt(n, m-1, memo)

    return memo[(n, m)]

print(gt(18,18))
