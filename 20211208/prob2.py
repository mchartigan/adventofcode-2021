'''
--- Part Two ---

Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

    acedgfb: 8
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    dab: 7
    cefabd: 9
    cdfgeb: 6
    eafb: 4
    cagedb: 0
    ab: 1

Then, the four digits of the output value can be decoded:

    cdfeb: 5
    fcadb: 3
    cdfeb: 5
    cdbaf: 3

Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

    fdgacbe cefdb cefbgd gcbe: 8394
    fcgedb cgb dgebacf gc: 9781
    cg cg fdcagb cbg: 1197
    efabcd cedba gadfec cb: 9361
    gecf egdcabf bgf bfgea: 4873
    gebdcfa ecba ca fadegcb: 8418
    cefg dcbef fcge gbcadfe: 4548
    ed bcgafe cdgba cbgef: 1625
    gbdfcae bgc cg cgb: 8717
    fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
'''

def getOutput(input, output):
    key = {'a': '','b': '','c': '','d': '','e': '','f': '','g': ''}
    trueFreq = {'a': 8,'b': 6,'c': 8,'d': 7,'e': 4,'f': 9,'g': 7}
    expFreq = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0}

    input.sort(key=lambda x: len(x))
    for string in input:
        for char in string:
            expFreq[char] += 1

    for letter, val in expFreq.items():
        if val == 4: key['e'] = letter 
        if val == 9: key['f'] = letter 
        if val == 6: key['b'] = letter

    key['c'] = input[0].replace(key['f'],'')
    key['a'] = input[1].replace(key['f'],'').replace(key['c'],'')
    key['d'] = input[2].replace(key['f'],'').replace(key['c'],'').replace(key['b'],'')
    key['g'] = [x for x in input[-1] if x not in key.values()][0]
    
    keys = list(key.keys())
    ciphs = list(key.values())
    for i in range(0,len(output)):
        output[i] = list(output[i])
        for j in range(0,len(output[i])):
            output[i][j] = keys[ciphs.index(output[i][j])]

    total = 0
    for i in range(len(output),0,-1):
        sortedStr = ''.join(sorted(output[len(output)-i]))
        if sortedStr == 'cf': total += 1*10**(i-1)
        elif sortedStr == 'acdeg': total += 2*10**(i-1)
        elif sortedStr == 'acdfg': total += 3*10**(i-1)
        elif sortedStr == 'bcdf': total += 4*10**(i-1)
        elif sortedStr == 'abdfg': total += 5*10**(i-1)
        elif sortedStr == 'abdefg': total += 6*10**(i-1)
        elif sortedStr == 'acf': total += 7*10**(i-1)
        elif sortedStr == 'abcdefg': total += 8*10**(i-1)
        elif sortedStr == 'abcdfg': total += 9*10**(i-1)

    return total

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

    inputs = []
    outputs = []
    grand = 0
    for line in lines:
        IOs = line.split(' | ')
        grand += getOutput(IOs[0].strip().split(' '),IOs[1].strip().split(' '))

    print(grand)
