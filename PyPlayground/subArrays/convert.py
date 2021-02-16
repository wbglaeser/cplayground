with open("testcase.txt", "r") as f:
    lines = f.readlines()

N = int(lines[0])
d = []
for i in range(1,2*N+1):
    if i % 2 == 0:
        print(i)
        d.append(list(map(int,lines[i].split())))



