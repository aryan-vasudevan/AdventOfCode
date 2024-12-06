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

res = 0
for order in orders:
    valid = True
    for i, n in enumerate(order):
        if n in precedences:
            for p in precedences[n]:
                if p in order:
                    if order.index(p) < i:
                        valid = False
    
    if valid:
        res += order[len(order) // 2]


print(res)