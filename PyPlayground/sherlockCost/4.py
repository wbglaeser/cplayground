def get_max_cost(B):
    N = len(B)
    hi,low=0,0
    for i in range(1, N): # note we skip index 0
        high_to_low_diff = abs(B[i-1] - 1)
        low_to_high_diff = abs(B[i] - 1)
        high_to_high_diff = abs(B[i] - B[i-1])

        low_next = max(low, hi+high_to_low_diff)
        
        if hi+high_to_high_diff > low+low_to_high_diff:
            hi_next = hi+high_to_high_diff
            print(B[i-1])
        else: 
            hi_next = low+low_to_high_diff
            print(B[i])

        print(f"1: {low}, {hi}")
        low = low_next
        hi = hi_next
        print(f"2: {low}, {hi}")
        

    return max(hi,low)

#a = [52, 60, 50, 90, 84, 35, 56, 64, 52, 20, 43, 19, 12, 73, 48, 93, 43, 78, 22, 53, 60, 100, 26, 54, 84]
#a = [59, 61, 78, 94]
a = [14, 30, 82, 49, 47, 96, 34, 66, 15, 11, 43, 45, 56, 77, 53, 13, 43, 92, 67, 37]
print(get_max_cost(a))
