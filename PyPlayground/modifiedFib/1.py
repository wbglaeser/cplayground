t1 = 0
t2 = 1
n = 5
fib = [0 for i in range(n)]
fib[0] = t1
fib[1] = t2

for i in range(2,n):
    fib[i] = fib[i-1]**2 + fib[i-2]

print(fib[n-1])
