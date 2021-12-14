import timeit

start = timeit.default_timer()

with open('05.txt') as f:
    lines = [line.rstrip() for line in f]

data = []
populate = []

for line in lines:
    parts = line.split(" -> ")
    coord1 = parts[0].split(",")
    coord2 = parts[1].split(",")
    data.append([coord1,coord2])

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
            num1 +=1
        diff -= 1

    



cleansed = []

for index in range(len(populate)):
    cleansed.append(','.join(populate[index]))

count = {i:cleansed.count(i) for i in cleansed}
overlap = {k:v for k,v in count.items() if v != 1}
print(len(overlap))

stop = timeit.default_timer()
print('Time: ', stop - start)
