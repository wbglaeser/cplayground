a = "asdsfdagrdgdfsdfdkkkg"
b = "dhffdgsdfgvdfbffdllg"

K = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]

for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]: K[i+1][j+1] = K[i+1][j] + 1
        else: K[i+1][j+1] = max(K[i+1][j], K[i][j+1])

print(K[-1][-1])
