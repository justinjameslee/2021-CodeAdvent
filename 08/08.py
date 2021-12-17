import timeit
import numpy as np
from numpy.core.fromnumeric import sort

start = timeit.default_timer()

with open('08.txt') as f:
    lines = [line.rstrip() for line in f]

data = []
for index in range(len(lines)):
    data.append(lines[index][lines[index].find("| ")+2:len(lines[index])].split(" "))

count = 0
for row in range(len(data)):
    for i in range(len(data[row])):
        if len(data[row][i]) == 2 : count += 1
        elif len(data[row][i]) == 4 : count += 1
        elif len(data[row][i]) == 3 : count += 1
        elif len(data[row][i]) == 7 : count += 1

print(count)

stop = timeit.default_timer()
print('Time: ', stop - start)