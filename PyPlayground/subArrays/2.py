def findArrs(a):
    n = len(a)

    # edge case
    ms = a[0]
    rs = 0
    for i in range(n):
        rs += a[i]
        if a[i] > rs: rs = a[i]
        if rs > ms: ms = rs

    maxsss = sum([x for x in a if x >= 0])
    if maxsss == 0: return print(arr)
    print(ms)
    print(maxsss)


with open("testcase.txt", "r") as f:
    lines = f.readlines()

N = int(lines[0])
d = []
#for i in range(1,2*N+1):
#    if i % 2 == 0:
#        a = list(map(int,lines[i].split()))
#        findArrs(a)
        
a = [2, -1, 2, 3, 4, -5]
n = len(a)
findArrs(a)


