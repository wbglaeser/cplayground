w = [0,0,0,0,0,0,0,0,0,0,0,0,0,11]

def computefc(w):

    res = waterFountain(len(w), w)
    if res > len(w): return "not possible"
    return res

def waterFountain(n, w, p=1, rIndex=0, count=0):
  
    # if we have reached boundary return high value
    if p > n: return n+1 
    
    # if current fountain does not connect to existing fountain leave off and move on
    if max(p - w[p-1], 1) > rIndex+1: return waterFountain(n,w,p+1,rIndex, count)
    
    # compute new right index
    _rIndex = min(p + w[p-1], n)

    # if new right index reaches end of garden return count with last fountain switched on
    if _rIndex == n: return count + 1 
 
    return min(
        waterFountain(n,w,p+1, _rIndex, count+1), # switch current fountain on and move forward
        waterFountain(n,w,p+1, rIndex, count), # leave fountain off and move forward
    )

print(computefc(w))
