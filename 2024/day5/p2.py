file = open("input.txt", "r")

precedences = {}
with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            break
        n1, n2 = [int(x) for x in line.split("|")]
        if n1 in precedences:
            precedences[n1].append(n2)
        else:
            precedences[n1] = [n2]

orders = []
with open("input.txt", "r") as file:
    for line in file:
        if "|" in line or line == "\n":
            continue
        orders.append([int(x) for x in line.split(",")])

def isValidOrder(order, precedences):
    for i, n in enumerate(order):
        if n in precedences:
            for p in precedences[n]:
                if p in order and order.index(p) < i:
                    return False
    return True

def fixOrder(order, precedences):
    graphSubset = {n: [] for n in order}
    for n in order:
        if n in precedences:
            for p in precedences[n]:
                if p in order:
                    graphSubset[n].append(p)

    inDegree = {n: 0 for n in order}
    for n in graphSubset:
        for p in graphSubset[n]:
            inDegree[p] += 1

    queue = [n for n in order if inDegree[n] == 0]
    sortedOrder = []

    while queue:
        current = queue.pop(0)
        sortedOrder.append(current)
        for neighbor in graphSubset[current]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.append(neighbor)

    return sortedOrder

res = 0
for order in orders:
    if not isValidOrder(order, precedences):
        newOrder = fixOrder(order, precedences)
        middleIndex = len(newOrder) // 2
        res += newOrder[middleIndex]

print(res)