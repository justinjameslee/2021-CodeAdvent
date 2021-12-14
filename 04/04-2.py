import numpy as np
import timeit

start = timeit.default_timer()

with open('04.txt') as f:
    lines = [line.rstrip() for line in f]

input = lines[0].split(",")

lines.pop(0)
temp = lines
data = []

for index in range(len(temp)):
    if temp[index] == "":
        temp1 = str(temp[index+1]).split()
        temp2 = str(temp[index+2]).split()
        temp3 = str(temp[index+3]).split()
        temp4 = str(temp[index+4]).split()
        temp5 = str(temp[index+5]).split()
        value = [temp1,temp2,temp3,temp4,temp5]
        data.append(value)
        index += 3
        if index >= len(temp):
            break

con01 = [["00"],["01"],["02"],["03"],["04"]]
con02 = [["10"],["11"],["12"],["13"],["14"]]
con03 = [["20"],["21"],["22"],["23"],["24"]]
con04 = [["30"],["31"],["32"],["33"],["34"]]
con05 = [["40"],["41"],["42"],["43"],["44"]]
con06 = [["00"],["10"],["20"],["30"],["40"]]
con07 = [["01"],["11"],["21"],["31"],["41"]]
con08 = [["02"],["12"],["22"],["32"],["42"]]
con09 = [["03"],["13"],["23"],["33"],["43"]]
con10 = [["04"],["14"],["24"],["34"],["44"]]

conditions = np.array([con01,con02,con03,con04,con05,con06,con07,con08,con09,con10])


flagged = []
index = 0

done = None
winningcard = 0
winningnum = 0

while index < len(input) and done == None:
    card = 0
    while card < len(data):
        for row in range(len(data[card])):
            for column in range(len(data[card][row])):
                if input[index] == data[card][row][column]:
                    flagged.append([card,[row,column]])
        card += 1

    test = 0
    while test < len(data):
        testTemp = []
        test2 = 0
        while test2 < len(flagged):
            if flagged[test2][0] == test:
                value = str(flagged[test2][1][0]) + str(flagged[test2][1][1])
                testTemp.append(value)
            test2 += 1

        conlen = 0
        while conlen < len(conditions):
            testTemp = np.array(testTemp)
            # if np.in1d(conditions[conlen].ravel(), testTemp.ravel()).all():
            if set(np.unique(conditions[conlen])).issubset(set(np.unique(testTemp))):
                winningcard = test
                winningnum = input[index]
                done = True
            conlen += 1
        test+=1
    index += 1


winningflagged = []
for index in range(len(flagged)):
    if flagged[index][0] == winningcard:
        winningflagged.append(flagged[index][1])

count = 0
flaggedsum = 0
while count < len(winningflagged):
    print(data[winningcard][winningflagged[count][0]])
    print(winningflagged[count][1])
    flaggedsum += int(data[winningcard][winningflagged[count][0]][winningflagged[count][1]])
    count += 1

intdata = [list(map(int,i)) for i in data[winningcard]]
print(intdata)

totalsum = sum(sum(intdata,[]))
unmarked = totalsum - flaggedsum

print(unmarked)
print(winningnum)

output = int(unmarked) * int(winningnum)
print(output)

stop = timeit.default_timer()
print('Time: ', stop - start)

