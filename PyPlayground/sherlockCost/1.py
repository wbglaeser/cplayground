def cost(B):
    cost = 0
    costa = 0  
    for i in range(1, len(B)):
        if i % 2 != 0: costa += abs(B[i] - 1)
        else: costa += abs(1-B[i-1]) 
    
    print(costa)

    costb = 0    
    for i in range(1, len(B)):
        if i % 2 == 0: costb += abs(B[i] - 1)
        else: costb += abs(1-B[i-1]) 
    
    print(costb)

    cost = 0
    for i in range(len(B)):
        

    return max(costa, costb)


a = [14, 30, 82, 49, 47, 96, 34, 66, 15, 11, 43, 45, 56, 77, 53, 13, 43, 92, 67, 37]
print(cost(a))
