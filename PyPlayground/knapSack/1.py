W = 5
wt = [5, 3, 4, 2]
v =  [60, 50, 70, 30]
#v = [a-b for a,b in zip(v,wt)]

def knapsack(W, wt, v, memo={}):
   
    if W in memo: return memo[W]

    new_val = 0
    for i in range(len(wt)):
        if W - wt[i] >= 0:
            _wt = wt[:i] + wt[i+1:]
            _v = v[:i] + v[i+1:]
            _nk = knapsack(W-wt[i], _wt, _v, memo)
            if v[i] + _nk > new_val:
                new_val = v[i] + _nk
    
    memo[W] = new_val
    return new_val

print(knapsack(W, wt, v))
