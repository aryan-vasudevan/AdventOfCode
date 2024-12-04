def xmas(grid, row, column):
    res = 0

    if row == 0 or column == 0 or row == len(grid) - 1 or column == len(grid[0]) - 1:
        return res

    diagonal1 = [grid[row - 1][column + 1], grid[row + 1][column - 1]]
    diagonal2 = [grid[row - 1][column - 1], grid[row + 1][column + 1]]
    print(diagonal1, diagonal2)

    if (
        (diagonal1 == ["M", "S"] or diagonal1 == ["S", "M"]) and
        (diagonal2 == ["M", "S"] or diagonal2 == ["S", "M"])
    ):
        res += 1
        
    return res

grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

result = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == "A":
            result += xmas(grid, row, column)

print(result)