leftList = []
rightList = []

while True:
    row = input()
    if row == "done":
        break

    int1, int2 = [int(x) for x in row.split()]
    leftList.append(int1)
    rightList.append(int2)

counts = {}
for i in rightList:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

score = 0
for i in leftList:
    if i not in counts:
        continue
    else:
        score += counts[i] * i

print(score)