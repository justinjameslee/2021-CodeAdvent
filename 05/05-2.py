import timeit

start = timeit.default_timer()

with open('05.txt') as f:
    lines = [line.rstrip() for line in f]

data = []
populate = []
diagdata = []

for line in lines:
    parts = line.split(" -> ")
    coord1 = parts[0].split(",")
    coord2 = parts[1].split(",")
    data.append([coord1, coord2])

for index in range(len(data)):
    constant = 0
    num1 = 0
    num2 = 0
    location = 0
    if data[index][0][0] == data[index][1][0]:
        constant = data[index][0][0]
        num1 = int(data[index][0][1])
        num2 = int(data[index][1][1])
        location = 0
        diff = abs(num1 - num2) + 1

    elif data[index][0][1] == data[index][1][1]:
        constant = data[index][0][1]
        num1 = int(data[index][0][0])
        num2 = int(data[index][1][0])
        location = 1
        diff = abs(num1 - num2) + 1
    
    else:
        diagdata.append(data[index])

    while diff > 0:
        if num1 >= num2:
            if location == 0:
                populate.append([constant, str(num2)])
            elif location == 1:
                populate.append([str(num2), constant])
            num2 += 1
        elif num1 <= num2:
            if location == 0:
                populate.append([constant, str(num1)])
            elif location == 1:
                populate.append([str(num1), constant])
            num1 += 1
        diff -= 1

# print(diagdata)
# print("\n")
# print(populate)
# print("\n")

for index in range(len(diagdata)):
    pos1 = None
    pos2 = None
    current00 = int(diagdata[index][0][0])
    current10 = int(diagdata[index][1][0])
    current01 = int(diagdata[index][0][1])
    current11 = int(diagdata[index][1][1])
    populate.append([str(current00),str(current01)])
    while current00 != current10 and current01 != current11:
        if current00 > current10:
            pos1 = "minus"
        else:
            pos1 = "plus"
        if current01 > current11:
            pos2 = "minus"
        else:
            pos2 = "plus"

        if pos1 == "minus" and pos2 == "minus":
            current00 -= 1
            current01 -= 1
            populate.append([str(current00),str(current01)])
        elif pos1 == "minus" and pos2 == "plus":
            current00 -= 1
            current01 += 1
            populate.append([str(current00),str(current01)])
        elif pos1 == "plus" and pos2 == "plus":
            current00 += 1
            current01 += 1
            populate.append([str(current00),str(current01)])
        elif pos1 == "plus" and pos2 == "minus":
            current00 += 1
            current01 -= 1
            populate.append([str(current00),str(current01)])
        
# print(populate)

cleansed = []
for index in range(len(populate)):
    cleansed.append(','.join(populate[index]))

count = {i: cleansed.count(i) for i in cleansed}
overlap = {k: v for k, v in count.items() if v != 1}
print(len(overlap))

stop = timeit.default_timer()
print('Time: ', stop - start)
