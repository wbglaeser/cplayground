def canSum(target, a, memo={}):
    print(memo) 
    if target in memo: return memo[target]
    
    if target == 0: return True

    if target < 0: 
        memo[target] = False
        return memo[target]

    memo[target] = False
    for v in a:

        memo[target] = memo[target] or canSum(target-v, a, memo)
   
    return memo[target]

print(canSum(7, [5, 3, 4, 7]))
