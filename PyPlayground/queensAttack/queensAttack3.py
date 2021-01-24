obstacles = {(ob[0],ob[1]) for ob in obst}

mvs, count = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)], 0

for m in mvs:
    cr, cc = r_q, c_q
    while (cr + m[0] >= 1 and cr + m[0] <= n) and (cc + m[1] >= 1 and cc + m[1] <= n):
        cr += m[0]
        cc += m[1]
        if (cr, cc) in obstacles:break
        count += 1

return count
