with open('03.txt') as f:
    lines = [line.rstrip() for line in f]

lenbinary = len(lines[0])
repeat = 0

data = []
data2 = []

for x in lines:
    data.append(list(x))
    data2.append(list(x))

while repeat < lenbinary:
    column = []
    for index in range(len(data)):
        column.append(data[index][repeat])
    
    if column.count("1") < column.count("0"):
        for index in range(len(data)):
            if data[index][repeat] != "0":
                data[index] = ""
    else:
        for index in range(len(data)):
            if data[index][repeat] != "1":
                data[index] = ""

    data = list(filter(None,data))
    if len(data) == 1:
        break
    repeat += 1

repeat = 0

while repeat < lenbinary:
    column = []
    for index in range(len(data2)):
        column.append(data2[index][repeat])
    
    if column.count("1") < column.count("0"):
        for index in range(len(data2)):
            if data2[index][repeat] != "1":
                data2[index] = ""
    else:
        for index in range(len(data2)):
            if data2[index][repeat] != "0":
                data2[index] = ""

    
    data2 = list(filter(None,data2))
    if len(data2) == 1:
        break
    repeat += 1

print(data)
print(data2)

data = int(''.join(data[0]),2)
data2 = int(''.join(data2[0]),2)

output = data * data2
print(output)