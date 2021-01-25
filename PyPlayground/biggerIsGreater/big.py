s = "fedcbabcd"
from bisect import bisect

def run(s):
    f = "no answer"
    s = s.rstrip("\n")
    for idx in range(1, len(s)):
        if any(x > s[len(s)-idx-1] for x in s[len(s)-idx:]):
            swx = bisect(sorted(s[len(s)-idx:]), s[len(s)-idx-1])
            end = sorted(s[len(s)-idx:])[:]
            end.pop(swx)
            f = s[:len(s)-idx-1] + sorted(s[len(s)-idx:])[swx] +  "".join(sorted(end + list(s[len(s)-idx-1]))) + "\n"
            break
    return f

with open("inputtestcase") as f:
    lines = f.readlines()

with open("inputtestans") as f:
    ans = f.readlines()

for idx, line in enumerate(lines):
    if run(line) != ans[idx]:
        print(repr(run(line)))
        print(repr(ans[idx]))

