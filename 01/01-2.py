with open('01.txt') as f:
    lines = [int(line.rstrip()) for line in f]

index = lines[0]
count = 0
for i in range(len(lines)):
    if i < len(lines)-3:
        sum = lines[i] + lines[i+1] + lines[i+2]
        sum2 = lines[i+1] + lines[i+2] + lines[i+3]
        if sum < sum2:
            count += 1

print(count)