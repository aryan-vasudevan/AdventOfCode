res = 0

def isValid(list):
    return list == sorted(list) or list == sorted(list, reverse=True)

def isSafe(list):
    for i in range(len(list) - 1):
        difference = abs(list[i + 1] - list[i])
        if difference > 3 or difference < 1:
            return False
    return True

while True:
    row = input()
    if row == "done":
        break

    row = [int(x) for x in row.split()]

    if isValid(row) and isSafe(row):
        res += 1
    else:
        foundSafe = False
        for i in range(len(row)):
            temp = row[:i] + row[i + 1:]
            if isValid(temp) and isSafe(temp):
                foundSafe = True
                break
        if foundSafe:
            res += 1

print(res)
