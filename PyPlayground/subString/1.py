a = "adfs"
b = "aef"

def subString(a,b, count=0, memo={}):
    if (a, b) in memo: 
        return memo[(a, b)]
    
    if len(a) == 0 or len(b) == 0: 
        memo[(a, b)] = 0
        return 0
    
    if a[-1] == b[-1]: 
        memo[(a, b)] = subString(a[:-1], b[:-1], memo) + 1
        return memo[(a,b)]
    return max(subString(a[:-1], b, memo), subString(a, b[:-1], memo))

print(subString(a, b))
