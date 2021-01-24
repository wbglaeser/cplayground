s = "dkhc"

s = list(s)

# first increase

for start_id in range(len(s))[::-1]:
    stop = 0
    for val in range(start_id)[::-1]:
        _s = s.copy()
        _s[start_id], _s[val] = _s[val], _s[start_id]
        if "".join(_s) > "".join(s):
            s = _s
            stop = 1
            break
    if stop == 1:
        break
print("".join(s))
