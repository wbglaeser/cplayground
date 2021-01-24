from itertools import combinations

k = 1
s = [1, 2, 3, 4, 5]

count = 0
d = {x:[] for x in range(k)}
for n in range(len(s)): d[s[n]%k].append(s[n])

if len(d[0]) > 0:
    count = 1

S = set([(x, k-x) for x in range(1, k//2+1)])
print(S)
for i,j in S:
    if i != j:
        if len(d[i]) > len(d[j]):
            count += len(d[i])
        else:
            count += len(d[j])
    else:
        if len(d[i]) > 0:
            count += 1
print(count)
