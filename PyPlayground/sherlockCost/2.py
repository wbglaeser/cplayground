def costD(B, A_prev=0, i=-1, cost=0):

    if A_prev != 0:
        costa = cost + abs(B[i] - A_prev)
        costb = cost + abs(1-A_prev)
    
    else:
        costa, costb = 0, 0
    
    B_prev_M = B[i]
    B_prev_L = 1

    if i == -len(B): return max(costa, costb)

    return max(
        costD(B, B_prev_M, i-1, costa),
        costD(B, B_prev_L, i-1, costb),
    )

a = [10, 1, 10, 1, 10]
print(costD(a))
