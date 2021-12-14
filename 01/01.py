with open('01.txt') as f:
    lines = [int(line.rstrip()) for line in f]

index = lines[0]
count = 0
for x in lines:
    if x > index:
        count += 1
    index = x

print(count)