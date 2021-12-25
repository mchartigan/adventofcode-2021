'''
--- Day 24: Arithmetic Logic Unit ---

Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU). Without the ability to perform basic arithmetic and logic functions, the submarine can't produce cool patterns with its Christmas lights!

It also can't navigate. Or run the oxygen system.

Don't worry, though - you probably have enough oxygen left to give you enough time to build a new ALU.

The ALU is a four-dimensional processing unit: it has integer variables w, x, y, and z. These variables all start with the value 0. The ALU also supports six instructions:

    inp a - Read an input value and write it to variable a.
    add a b - Add the value of a to the value of b, then store the result in variable a.
    mul a b - Multiply the value of a by the value of b, then store the result in variable a.
    div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
    mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
    eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.

In all of these instructions, a and b are placeholders; a will always be the variable where the result of the operation is stored (one of w, x, y, or z), while b can be either a variable or a number. Numbers can be positive or negative, but will always be integers.

The ALU has no jump instructions; in an ALU program, every instruction is run exactly once in order from top to bottom. The program halts after the last instruction has finished executing.

(Program authors should be especially cautious; attempting to execute div with b=0 or attempting to execute mod with a<0 or b<=0 will cause the program to crash and might even damage the ALU. These operations are never intended in any serious ALU program.)

For example, here is an ALU program which takes an input number, negates it, and stores it in x:

inp x
mul x -1

Here is an ALU program which takes two input numbers, then sets z to 1 if the second input number is three times larger than the first input number, or sets z to 0 otherwise:

inp z
inp x
mul z 3
eql z x

Here is an ALU program which takes a non-negative integer as input, converts it into binary, and stores the lowest (1's) bit in z, the second-lowest (2's) bit in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's) bit in w:

inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2

Once you have built a replacement ALU, you can install it in the submarine, which will immediately resume what it was doing when the ALU failed: validating the submarine's model number. To do this, the ALU will run the MOdel Number Automatic Detector program (MONAD, your puzzle input).

Submarine model numbers are always fourteen-digit numbers consisting only of digits 1 through 9. The digit 0 cannot appear in a model number.

When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen separate inp instructions, each expecting a single digit of the model number in order of most to least significant. (So, to check the model number 13579246899999, you would give 1 to the first inp instruction, 3 to the second inp instruction, 5 to the third inp instruction, and so on.) This means that when operating MONAD, each input instruction should only ever be given an integer value of at least 1 and at most 9.

Then, after MONAD has finished running all of its instructions, it will indicate that the model number was valid by leaving a 0 in variable z. However, if the model number was invalid, it will leave some other non-zero value in z.

MONAD imposes additional, mysterious restrictions on model numbers, and legend says the last copy of the MONAD documentation was eaten by a tanuki. You'll need to figure out what MONAD does some other way.

To enable as many submarine features as possible, find the largest valid fourteen-digit model number that contains no 0 digits. What is the largest model number accepted by MONAD?
'''

inp = '8'

def isNum(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

class ALU:
    def __init__(self, inp):
        self.inp = inp
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        self.i = 0

    def newInput(self, inp):
        self.inp = inp
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        self.i = 0

    def parse(self, cmd):
        if cmd[0] == 'inp':
            self.__dict__[cmd[1]] = int(self.inp[self.i])
            self.i += 1

        elif cmd[0] == 'add':
            self.__dict__[cmd[1]] += int(cmd[2]) if isNum(cmd[2]) else self.__dict__[cmd[2]]

        elif cmd[0] == 'mul':
            self.__dict__[cmd[1]] *= int(cmd[2]) if isNum(cmd[2]) else self.__dict__[cmd[2]]

        elif cmd[0] == 'div':
            temp = self.__dict__[cmd[1]] / int(cmd[2]) if isNum(cmd[2]) else self.__dict__[cmd[1]] / self.__dict__[cmd[2]]
            self.__dict__[cmd[1]] = int(temp)

        elif cmd[0] == 'mod':
            self.__dict__[cmd[1]] %= int(cmd[2]) if isNum(cmd[2]) else self.__dict__[cmd[2]]

        elif cmd[0] == 'eql':
            if isNum(cmd[2]):
                self.__dict__[cmd[1]] = 1 if self.__dict__[cmd[1]] == int(cmd[2]) else 0
            else:
                self.__dict__[cmd[1]] = 1 if self.__dict__[cmd[1]] == self.__dict__[cmd[2]] else 0

    def parseAll(self, cmds):
        for cmd in cmds:
            self.parse(cmd)

        return (self.w, self.x, self.y, self.z)


with open("input.txt") as file:
    cmds = [x.strip().split(' ') for x in file.readlines() if x.strip() != '']

pts = []
for i in range(0, 14):
    a = 0
    b = 0
    c = 0
    for j in range(0, 18):
        if j == 4 and cmds[18*i + j][2]:
            a = cmds[18*i + j][2]
        if j == 5 and cmds[18*i + j][2]:
            b = cmds[18*i + j][2]
        if j == 15 and cmds[18*i + j][2]:
            c = cmds[18*i + j][2]
    pts.append((int(a),int(b),int(c)))

print(pts)

'''
i_2 + 2 - 0 = i_3
i_6 + 13 - 8 = i_7
i_5 + 4 - 9 = i_8
i_9 + 1 = i_10
i_4 + 11 - 5 = i_11
i_1 + 13 - 6 = i_12
i_0 + 8 - 12 = i_13

i_3 = i_2 + 2
i_7 = i_6 + 5
i_8 = i_5 - 5
i_10 = i_9 + 1
i_11 = i_4 + 6
i_12 = i_1 + 7
i_13 = i_0 - 4

max = [9,2,7,9,3,9,4,9,4,8,9,9,9,5]
min = [5,1,1,3,1,6,1,6,1,1,2,7,8,1]
'''
'''
modelNum = 99999999999999
alu = ALU(str(modelNum))

while True:
    _, _, _, z = alu.parseAll(cmds)
    if z == 0:
        print(modelNum)
        break
    else:
        modelNum -= 1
        alu.newInput(str(modelNum))


print(alu.parseAll(cmds))
'''