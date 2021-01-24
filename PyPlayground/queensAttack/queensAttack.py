n = 4 
k = 0
r_q = 4 
c_q = 4
obstacles = [
    [4,3],[2,2] 
]

options = 0
d = [True] * 8
step = 1
while True in d:
    print(d)
    # check v1
    if d[0]:
        if (r_q + step <= n) and ([r_q + steps, c_q] not in obstacles): 
            options += 1
        else: d[0] = False
    
    # check v2
    if d[1]:
        if (r_q - step >= 1) and ([r_q - step, c_q] not in obstacles): 
            options += 1
        else: d[1] = False

    # check h1
    if d[2]:
        if (c_q + step <= n) and ([r_q, c_q + step] not in obstacles): 
            options += 1
        else: d[2] = False

    # check h2
    if d[3]:
        if (c_q - step >= 1) and ([r_q, c_q - step] not in obstacles): 
            options += 1
        else: d[3] = False

    # check d1
    if d[4]:
        if (r_q + step <= n) and (c_q + step <= n) and ([r_q + step, c_q + step] not in obstacles): 
            options += 1
        else: d[4] = False

    # check d2
    if d[5]:
        if (r_q - step >= 1) and (c_q - step >= 1) and ([r_q - step, c_q - step] not in obstacles): 
            options += 1
        else: d[5] = False
    
    # check d3
    if d[6]:
        if (r_q + step <= n) and (c_q - step >= 1) and ([r_q + step, c_q - step] not in obstacles): 
            options += 1
        else: d[6] = False
    
    # check d4
    if d[7]:
        if (r_q - step >= 1) and (c_q + step <= n) and ([r_q - step, c_q + step] not in obstacles): 
            options += 1
        else: d[7] = False
     
    step += 1   
 
print(options)
