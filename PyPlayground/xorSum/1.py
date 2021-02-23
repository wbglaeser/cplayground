fsum = 0
N = 314159
a = 2
b = 10
M = 10**9 + 7
a = 394973741
b = 979985167

a_ = a % M
for i in range(N+1):
    if i == 0:
        _b = b % M
    else: 
        _b = (_b * 2) % M
    
    if i < len("{:b}".format(a)):
        fsum += (a ^ _b) % M
    else:
        fsum += (a + _b) % M

print(fsum % M)
