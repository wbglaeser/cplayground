def canSum(target, a, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target <= 0: 
        memo[target] = False
        return memo[target]

    for v in a:
        if canSum(target-v,a, memo): 
            return True

    memo[target] = False
    return memo[target]
    

print(canSum(7, [2,3], {}))
print(canSum(7, [5,3,4,7], {}))
print(canSum(7, [2,4], {}))
print(canSum(8, [2,3,5], {}))
print(canSum(300, [7,14], {}))
