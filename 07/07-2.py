import timeit
import numpy as np

start = timeit.default_timer()

with open('07.txt') as f:
    lines = [line.rstrip() for line in f]

data = lines[0].split(",")
data = np.asarray(data, dtype=int)
# avg = int(np.average(data))
index = 0
lowestsum = 0

while index < np.max(data):
    sum = 0
    for i in range(len(data)):
        n = int(abs(data[i] - index))
        formula = (n * (n + 1)) / 2
        sum += formula
    if sum < lowestsum or index == 0:
        lowestsum = sum
    index += 1

print(lowestsum)


stop = timeit.default_timer()
print('Time: ', stop - start)