import re

def processMemory(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    matches = re.findall(pattern, memory)

    total = sum(int(x) * int(y) for x, y in matches)
    
    return total

inp = ""
with open('input.txt', 'r') as file:
    for line in file:
        inp += line

print(processMemory(inp))