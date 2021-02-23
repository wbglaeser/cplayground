def xorAndSum(a, b):
    x=int(a,2)
    y=int(b,2)
    p=0
    for i in range(0,314160):
        p+=x^(y<<i)
    return p%((10**9)+7)

