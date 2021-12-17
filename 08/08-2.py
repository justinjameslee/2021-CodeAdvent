import timeit
import numpy as np
from numpy.core.fromnumeric import sort

start = timeit.default_timer()

with open('08.txt') as f:
    lines = [line.rstrip() for line in f]

def find_difference(first_set, second_set):
    return first_set.symmetric_difference(second_set)

def flatten(array):
    flatten = [item for sublist in array for item in sublist]
    count = {i: flatten.count(i) for i in flatten}
    reverse = {}
    for key, value in count.items():
        if value in reverse:
            reverse[value].append(key)
        else:
            reverse[value]=[key]
    return reverse

def swapkeyvalue(dictionary):
    return {v: k for k, v in dictionary.items()}

def find_letter_d(num4, num235):
    num235.append(num4)
    totalChar = []
    for i in range(len(num235)):
        totalChar.append(list(num235[i]))
    reverse = flatten(totalChar)
    return ''.join(reverse.get(4))

def find_letter_g(numdict, letterdict):
    totalChar = []
    totalChar.append(list(numdict[2]))
    totalChar.append(list(numdict[3]))
    totalChar.append(list(numdict[5]))
    reverse = flatten(totalChar)
    adg = ''.join(reverse.get(3))
    return ''.join(find_difference(set(letterdict['a'] + letterdict['d']), set(adg)))

def find_letter_c_f(numdict, letterdict):
    output = {}
    output['f'] = ''.join(find_difference(set(letterdict['a'] + letterdict['b'] + letterdict['d'] + letterdict['g']), set(numdict[5])))
    output['c'] = ''.join(find_difference(set(output['f']), set(numdict[1])))
    return output

def find_number_2_3_5(numdict, letterdict, num235):
    output = {}
    for i in range(len(num235)):
        if letterdict['b'] in num235[i]:
            output[5] = num235[i]
    num235.remove(output[5])
    num23 = num235
    relevantletters = numdict.get(1)
    relevantletters += letterdict.get('d')
    relevantletters = list(relevantletters)
    relevantletters = np.asarray(relevantletters)
    for i in range(len(num23)):
        current = np.asarray(list(num23[i]))
        if set(np.unique(relevantletters)).issubset(set(np.unique(current))):
            output[3] = num23[i]
    num23.remove(output[3])
    output[2] = num23[0]
    return output

def find_number_0_6_9(letterdict, num069):
    output = {}
    for i in range((len(num069))):
        if letterdict['d'] not in num069[i]:
            output[0] = num069[i]
    num069.remove(output[0])
    num69 = num069
    for i in range((len(num69))):
        if letterdict['c'] not in num69[i]:
            output[6] = num69[i]
        else:
            output[9] = num69[i]
    return output

def alpha_sort(array):
    output = []
    for sublist in array:
        temp = []
        for i in range(len(sublist)):
            split = list(sublist[i])
            split = ''.join(sorted(split))
            temp.append(split)
        output.append(temp)
    return output

input = []
data = []
for index in range(len(lines)):
    data.append(lines[index][lines[index].find("| ")+2:len(lines[index])].split(" "))
    input.append(lines[index][0:lines[index].find(" | ")].split(' '))

input = alpha_sort(input)
data = alpha_sort(data)

totalsum = 0
for row in range(len(data)):
    count = ''
    input[row].sort(key=len)
    numdict = {
        1 : input[row][0], 7 : input[row][1], 4 : input[row][2], 8 : input[row][9]
    }
    letterdict = {
        'a' : ''.join(find_difference(set(input[row][0]), set(input[row][1]))),
        'd' : find_letter_d(input[row][2], [input[row][3],input[row][4],input[row][5]])
    }
    letterdict['b'] = ''.join(find_difference(set(numdict[4]), set(numdict[1] + letterdict['d'])))
    numdict[2] = find_number_2_3_5(numdict,letterdict,[input[row][3],input[row][4],input[row][5]]).get(2)
    numdict[3] = find_number_2_3_5(numdict,letterdict,[input[row][3],input[row][4],input[row][5]]).get(3)
    numdict[5] = find_number_2_3_5(numdict,letterdict,[input[row][3],input[row][4],input[row][5]]).get(5)
    letterdict['g'] = find_letter_g(numdict, letterdict)
    letterdict['c'] = find_letter_c_f(numdict, letterdict).get('c')
    letterdict['f'] = find_letter_c_f(numdict, letterdict).get('f')
    numdict[0] = find_number_0_6_9(letterdict, [input[row][6],input[row][7],input[row][8]]).get(0)
    numdict[6] = find_number_0_6_9(letterdict, [input[row][6],input[row][7],input[row][8]]).get(6)
    numdict[9] = find_number_0_6_9(letterdict, [input[row][6],input[row][7],input[row][8]]).get(9)

    # print(input[row])
    # print(letterdict)
    # print(data[row])

    numdict = swapkeyvalue(numdict)
    #print(numdict)
    for i in range(len(data[row])):
        count += str(numdict[data[row][i]])
    #print(count)
    totalsum += int(count)
    #print(totalsum)

print(totalsum)

stop = timeit.default_timer()
print('Time: ', stop - start)