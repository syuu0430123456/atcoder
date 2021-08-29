maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

#スタート位置をセット
pos = [[1, 1, 0]]

while len(pos) > 0:
    x, y, depth = pos.pop(0)

    #ゴールにつくと終了
    if maze[x][y] == 1:
        print(depth)
        break

    #探索済みとしてセット
    maze[x][y] = 2

    #上下左右を探索
    if maze[x-1][y] < 2:
        pos.append([x-1, y, depth + 1])
    if maze[x+1][y] < 2:
        pos.append([x+1, y, depth + 1])
    if maze[x][y-1] < 2:
        pos.append([x, y-1, depth + 1])
    if maze[x][y+1] < 2:
        pos.append([x, y+1, depth + 1])