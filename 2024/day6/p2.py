seen = set()

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

def simulateGuard(grid, x, y, curDir):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    turns = 0
    seenStates = set()
    while True:
        state = (x, y, curDir)
        if state in seenStates:
            return True
        seenStates.add(state)
        x, y, inside = move(grid, x, y, directions[curDir], True)
        if not inside or grid[y + directions[curDir][1]][x + directions[curDir][0]] == "#":
            curDir = (curDir + 1) % 4
            turns += 1
        if not inside:
            return False

def findValidObstructions(grid, startX, startY, startDir):
    validPositions = []
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == "." and (x, y) != (startX, startY):
                grid[y][x] = "#"
                if simulateGuard(grid, startX, startY, startDir):
                    validPositions.append((x, y))
                grid[y][x] = "."
    return validPositions

grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

startX, startY, startDir = None, None, None
directionMap = {"^": 0, ">": 1, "v": 2, "<": 3}
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] in directionMap:
            startX, startY = col, row
            startDir = directionMap[grid[row][col]]
            grid[row][col] = "."

validPositions = findValidObstructions(grid, startX, startY, startDir)
print(len(validPositions))