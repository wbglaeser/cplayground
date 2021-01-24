import bisect
import time

n = 1000
k = 0
r_q = 400
c_q = 477

with open("queen_data.txt", "r") as f:
    lines = f.readlines()
obstacles = []
for l in lines:
    obstacles.append([int(x) for x in l.replace("\n", "").split(" ")])

options = 0
t0 = time.time()
if n == 1: options = 0
elif len(obstacles) == 0:
    options += 2 * (n-1)
    options += n - abs(r_q-c_q) - 1
    options += n - abs((n-r_q+1) - c_q) - 1

else:
    hv_ = sorted([x[1] for x in obstacles if x[0] == r_q])
    if len(hv_) == 0:
        options += n - 1
    else:
        hv = [0] + hv_ + [n]
        q = bisect.bisect_left(hv, c_q)
        print(hv_)
        options += (hv[q] - hv[q-1]) - 1 + (hv_[0] > c_q) - (hv_[-1] > c_q)
        print(hv_[0] > c_q) 
        print(hv_[-1] > c_q) 
        print(options) 
    vv_ = sorted([x[0] for x in obstacles if x[1] == c_q])
    if len(vv_) == 0:
        options += n - 1
    else:
        vv = [0] + vv_ + [n]
        print(vv_)
        q = bisect.bisect_left(vv, r_q)
        options += (vv[q] - vv[q-1]) - 1 + (vv_[0] > r_q) - (vv_[-1] > r_q)
        print(options - 676)
    total = time.time() - t0
    
    t1 = time.time()
    d = [True] * 4
    step = 1
    while True in d:

        # check d1
        if d[0]:
            if (r_q + step <= n) and (c_q + step <= n) and ([r_q + step, c_q + step] not in obstacles): 
                options += 1
            else: d[0] = False

        # check d2
        if d[1]:
            if (r_q - step >= 1) and (c_q - step >= 1) and ([r_q - step, c_q - step] not in obstacles): 
                options += 1
            else: d[1] = False
    
        # check d3
        if d[2]:
            if (r_q + step <= n) and (c_q - step >= 1) and ([r_q + step, c_q - step] not in obstacles): 
                options += 1
            else: d[2] = False
    
        # check d4
        if d[3]:
            if (r_q - step >= 1) and (c_q + step <= n) and ([r_q - step, c_q + step] not in obstacles): 
                options += 1
            else: d[3] = False
    
        step += 1
    total_ = time.time()-t1

print(total)
print(total_)
print(total/(total + total_))
print(total_/(total + total_))
print(options)
