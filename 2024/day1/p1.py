leftList = []
rightList = []

while True:
    row = input()
    if row == "done":
        break

    int1, int2 = [int(x) for x in row.split()]
    leftList.append(int1)
    rightList.append(int2)

leftList.sort()
rightList.sort()

distances = []

for i in range(1000):
    distances.append(abs(leftList[i] - rightList[i]))

print(sum(distances))