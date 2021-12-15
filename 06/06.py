import timeit

start = timeit.default_timer()

with open('06-sample.txt') as f:
    lines = [line.rstrip() for line in f]

data = lines[0].split(",")
print(data)
