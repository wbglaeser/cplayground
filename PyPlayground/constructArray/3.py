n = 49896
k = 67726
x = 39965
M = 1000000007

for i in range(n-2):

    if i == 0:
        mx = 0
        mo = 1

    _mx = (k-1) * (mo % M) % M
    mo = ((k-2) * (mo % M) + 1 * (mx % M)) % M
    mx = _mx

if (x == 1):
    print(mx)
else: print(mo)

