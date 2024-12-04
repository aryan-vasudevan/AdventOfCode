def dfs(grid, row, column):
    path = ["M", "A", "S"]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    res = 0

    for direction in directions:
        validPath = True
        for i in range(1, 4):
            newRow = row + i * direction[0]
            newCol = column + i * direction[1]

            if (
                newRow < 0 or newRow >= len(grid) or
                newCol < 0 or newCol >= len(grid[0]) or
                grid[newRow][newCol] != path[i - 1]
            ):
                validPath = False
                break

        if validPath:
            res += 1

    return res

grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

res = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == "X":
            res += dfs(grid, row, column)

print(res)