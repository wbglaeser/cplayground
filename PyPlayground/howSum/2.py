def howSum(target, a, memo={}):

    if target in memo: return None
    if target == 0: return [] 
    if target < 0: 
        memo[target] = None
        return None

    for v in a:
        res = howSum(target-v, a, memo)
        if not res == None:
            return [v] + res
  
    memo[target] = None
    return None

print(howSum(7, [3,2], {}))
print(howSum(7, [5, 3, 4, 7], {}))
print(howSum(7, [2,4], {}))
print(howSum(8, [2,3,5],{}))
print(howSum(300, [7,14],{}))
