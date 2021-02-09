amount = 4
coins = [1,2,3]
K = [[-1 for j in range(amount+1)] for i in range(len(coins)+1)]

for a in range(1,amount+1):
    for i,c in enumerate(coins):
        if (c - K[a-c][i+1]) == a: K[a][i+1] += 1
        else: K[a][i] = K[a-1][i]
        print(K)

