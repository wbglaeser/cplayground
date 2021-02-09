W = 4
wt = [1, 2, 3]
count = 0
s = []
d = {}

def ks(W, wt, count, s, d):

    for j in wt:
        print(f"{j}, {W}")
       
        if W-j > 0:
            if j not in d: d[j] = 1
            else: d[j] += 1
            ks(W-j, wt, count, s, d)

        if (W-j == 0):  
            d[j] += 1
            s.append(d)
            print(s)
            print("update count")

ks(W, wt, count, s, d)
print(count)
