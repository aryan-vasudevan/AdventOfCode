seen = {}

def move(grid, x, y, dir, inside):
    while inside:
        nextX = x + dir[0]
        nextY = y + dir[1]

        if nextY < 0 or nextY >= len(grid) or nextX < 0 or nextX >= len(grid[0]):
            inside = False
            return x, y, inside

        if grid[nextY][nextX] == "#":
            return x, y, inside

        x = nextX
        y = nextY

        seen.add((x, y))

    return x, y, inside



grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line)[:-1])

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != "^":
            continue
        else:
            x, y = col, row
            seen = {(x, y)}

inside = True
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
turns = 0
curDir = 0

while inside:
    x, y, inside = move(grid, x, y, directions[curDir], inside)
    curDir = (curDir + 1) % 4
    turns += 1

print(turns//3)
print(len(seen))