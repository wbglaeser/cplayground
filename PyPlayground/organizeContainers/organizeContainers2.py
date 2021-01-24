import os

def organiyeContainers(container):
    result = "Possible"
    for tp in range(len(c)):
        _missing = sum([c[x][tp] for x in range(len(c)) if x != tp])
        _tradeble = sum([c[tp][x] for x in range(len(c)) if x != tp])
        if _missing != _tradeble:
            result = "Impossible"
            break
    print(result)
    return result

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result + '\n')

