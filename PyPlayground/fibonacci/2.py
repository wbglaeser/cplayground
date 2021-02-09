def fib(n):
    a = [-1 for v in range(n)]
    a[0] = 1
    a[1] = 1
    for v in range(2,n):
        a[v] = a[v-2] + a[v-1]
    return a[n-1]

print(fib(1))
