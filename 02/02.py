with open('02.txt') as f:
    lines = [line.rstrip() for line in f]

horizontal = 0
depth = 0

for x in lines:
    data = x.split()
    if data[0] == "forward":
        horizontal += int(data[1])
    elif data[0] == "down":
        depth += int(data[1])
    elif data[0] == "up":
        depth -= int(data[1])

output = horizontal * depth
print(output)