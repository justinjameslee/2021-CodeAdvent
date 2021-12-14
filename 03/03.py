with open('03.txt') as f:
    lines = [line.rstrip() for line in f]

gamma = []

lenbinary = len(lines[0])
repeat = 0

while repeat < lenbinary:
    column = []
    for x in lines:
        data = list(x)
        column.append(data[repeat])
    if column.count("1") > column.count("0"):
        gamma.append("1")
    elif column.count("1") < column.count("0"):
        gamma.append("0")
    else:
        gamma.append("test")
    repeat += 1

index = 0
epsilon = []
while index < lenbinary:
    if gamma[index] == "1":
        epsilon.append("0")
    else:
        epsilon.append("1")
    index += 1

gamma = int(''.join(gamma),2)
epsilon = int(''.join(epsilon),2)

output = gamma * epsilon
print(output)