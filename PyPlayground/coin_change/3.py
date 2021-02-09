W = 4
wt = [1, 2, 3]
count = 0
dp = [[[-1] * W for i in range(len(wt))] for x in range(len(wt))]
print(dp)

for j in range(len(wt) + 1):
    for v in wt[j:]:
        for w in range(W + 1):
            if (j == 0) or (w == 0):


            print(j, v, w)
