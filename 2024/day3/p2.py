import re

def processMemory(memory):
    mulPattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"do\(\)|don't\(\)"

    mulEnabled = True
    total = 0

    for match in re.finditer(f"{mulPattern}|{control_pattern}", memory):
        command = match.group(0)

        if command == "do()":
            mulEnabled = True
        elif command == "don't()":
            mulEnabled = False

        elif command.startswith("mul") and mulEnabled:
            a, b = map(int, match.groups()[:2])
            total += a * b

    return total

inp = ""
with open("input.txt", "r") as file:
    inp = file.read()

print(processMemory(inp))
