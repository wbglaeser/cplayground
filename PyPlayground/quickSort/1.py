from random import randrange
a = [3,1,2,5]

def partition(a):
    
    # pick pivot and swap to end of array
    _pi = randrange(len(a))
    p = a[_pi]
    del a[_pi]
    a += [p]

    # run partitioning
    pi = 0
    for i in range(len(a)):
        if (a[i] <= p):
            a[i], a[pi] = a[pi], a[i] 
            pi += 1
    
    return a

print("final: ", partition([3,7,1,4]))
