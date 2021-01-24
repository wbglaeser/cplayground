from itertools import combinations, product

k = 7
s = [
    278, 576, 
    496, 727, 
    410, 124, 
    338, 149, 
    209, 702, 
    282, 718,
    771, 575,
    436
]

def verify_subs(ss, k):
    for idx, val in enumerate(ss):
        for _val in ss[idx+1:]:
            if (val + _val) % k == 0: return False
    return True

max = None
new_arr = [x % k for x in s]
for id in range(len(s)):
    combos = product(new_arr)
    #for combo in combos:
    #    if verify_subs(combo, k):
    #        max = len(s)-id
    #        break
    #if max:
    #    break
    print(combos)
print(max)


