W = 30
wt = [1,2,4,6]
v = [5,3,5,6]
v = [a-b for a,b in zip(v, wt)]
K = [[0 for i in range(W + 1)] for j in range(len(wt)+1)]

for w in range(1, W+1):
    for k in range(len(wt)):
        if wt[k] > w: K[k+1][w] = K[k][w]
        else:
            K[k+1][w] = max(v[k]+K[k][w-wt[k]], K[k][w])

for line in K: print(line)
print(K[-1][-1])
