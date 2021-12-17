import timeit
import numpy as np

start = timeit.default_timer()

with open('06.txt') as f:
    lines = [line.rstrip() for line in f]

data = lines[0].split(",")
data = np.asarray(data, dtype=int)

(unique, counts) = np.unique(data, return_counts=True)
count = np.asarray((unique, counts)).T

population = [0, count[0][1], count[1][1], count[2][1], count[3][1], count[4][1], 0, 0, 0]
day = 0
totalfish = 0
while day < 256:
    newfish = population[0]
    population = population[1:]
    population.append(newfish)
    population[6] += newfish
    totalfish = sum(population)
    day += 1
    stop = timeit.default_timer()
    print('Day: ', day, ' | Running Time: ', stop - start)


print(totalfish)

stop = timeit.default_timer()
print('Time: ', stop - start)