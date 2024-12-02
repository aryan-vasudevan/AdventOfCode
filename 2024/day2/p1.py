res = 0

def valid(list):
    return list == sorted(list) or list == sorted(list, reverse=True)

while True:
    row = input()
    if row == "done":
        break

    row = [int(x) for x in row.split()]

    if valid(row):
        safe = True
        for i in range(len(row) - 1):
            difference = abs(row[i + 1] - row[i])
            if difference > 3 or difference < 1:
                safe = False
                break
        if safe:
            res += 1

print(res)
