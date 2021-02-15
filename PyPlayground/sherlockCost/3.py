def cost(B):
    
    costa = 0  
    for i in range(1, len(B)):
        _new_val = 0    
        if i == len(B)-1:
            _new_val = max(abs(B[i] - B[i-1]), abs(B[i-1] - 1))
        else:
            if i % 2 != 0: _new_val = abs(B[i] - 1)
            else: _new_val = abs(1-B[i-1]) 
        costa += _new_val
        print("costa: ", costa)
    
    costb = 0    
    for i in range(1,len(B)):
        if i == len(B)-1:
            costb += max(abs(B[i] - B[i-1]), abs(B[i-1] - 1))
        else:
            if i % 2 == 0: costb += abs(B[i] - 1)
            else: costb += abs(1-B[i-1]) 

        print("costb: ", costb)
    print("costa", costa)
    print("costb", costb)
    return max(costa, costb)

#a = [52, 60, 50, 90, 84, 35, 56, 64, 52, 20, 43, 19, 12, 73, 48, 93, 43, 78, 22, 53, 60, 100, 26, 54, 84]
#a = [59, 61, 78, 94]
a = [14, 30, 82, 49, 47, 96, 34, 66, 15, 11, 43, 45, 56, 77, 53, 13, 43, 92, 67, 37]
print(cost(a))
