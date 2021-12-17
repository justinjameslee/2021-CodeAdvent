import timeit
import numpy as np

start = timeit.default_timer()

with open('06.txt') as f:
    lines = [line.rstrip() for line in f]

data = lines[0].split(",")
data = np.asarray(data, dtype=int)

day = 0
while day < 80:
    for index in range(len(data)):
        if data[index] == 0:
            data = np.append(data, [8])
            data[index] = 6
        else:
            data[index] = data[index] - 1
    day += 1
    stop = timeit.default_timer()
    print('Day: ', day, ' | Running Time: ', stop - start)

print(len(data))

stop = timeit.default_timer()
print('Time: ', stop - start)