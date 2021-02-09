def fib(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    v = fib(n-1, memo) + fib(n-2, memo)
    memo.update({n: v})

    return v

print(fib(10))
