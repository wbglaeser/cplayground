k = 5
s = [
    770528134, 663501748, 384261537, 800309024,
    103668401, 538539662, 385488901, 101262949,
    557792122, 46058493
]
lsb = []

for idx, v in enumerate(s):
    _lsb = [v]
    for _v in s[idx+1:]:
        add = 1
        for __v in _lsb:
            if (_v + __v) % k == 0: 
                add = 0
                break
        if add == 1:
            _lsb.append(_v)
    if len(_lsb) > len(lsb):
        lsb = _lsb.copy()

print("final array: ", lsb)
print(len(lsb))
