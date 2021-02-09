with open("queen_data.txt", "r") as f:
    lines = f.readlines()

obstacles = []
for l in lines:
    obstacles.append([int(x) for x in l.replace("\n", "").split(" ")])
    print(obstacles)
