'''
--- Part Two ---

Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.

Literal values (type ID 4) represent a single number as described above. The remaining type IDs are more interesting:

    Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
    Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
    Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.

Using these rules, you can now work out the value of the outermost packet in your BITS transmission.

For example:

    C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
    04005AC33890 finds the product of 6 and 9, resulting in the value 54.
    880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
    CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
    D8005AC2A8F0 produces 1, because 5 is less than 15.
    F600BC2D8F produces 0, because 5 is not greater than 15.
    9C005AC2F8F0 produces 0, because 5 is not equal to 15.
    9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.

What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?
'''

from functools import reduce

class Packet:
    def __init__(self, ver, typ, vals, opType=None):
        self.ver = ver
        self.typ = typ
        self.vals = vals
        self.opType = opType

    def sumVersions(self):
        total = self.ver
        for val in self.vals:
            if isinstance(val, Packet):
                total += val.sumVersions()

        return total

    def getValue(self):
        if self.typ == 4:
            return self.vals[0]
        else:
            vallist = [val.getValue() for val in self.vals]
            if self.typ == 0:
                return sum(vallist)
            elif self.typ == 1:
                return reduce(lambda x,y: x*y, vallist)
            elif self.typ == 2:
                return min(vallist)
            elif self.typ == 3:
                return max(vallist)
            elif self.typ == 5:
                return 1 if vallist[0] > vallist[1] else 0
            elif self.typ == 6:
                return 1 if vallist[0] < vallist[1] else 0
            elif self.typ == 7:
                return 1 if vallist[0] == vallist[1] else 0

def readPacket(msg, single=False):
    i = 0
    pkts = []
    while i < len(msg) - 7:
        data = []
        op = None
        ver = int(msg[i:i+3], base=2)
        i += 3
        typ = int(msg[i:i+3], base=2)
        i += 3
        grps = []
        if typ == 4:
            while msg[i] != '0':
                grps.append(msg[i+1:i+5])
                i += 5
            grps.append(msg[i+1:i+5])
            i += 5

            data.append(int(''.join(grps), base=2))
        else:
            subdata = []
            if msg[i] == '0':
                length = int(msg[i+1:i+16], base=2)
                i += 16
                submsg = msg[i:i+length]
                
                j = 0
                while j < length - 4:
                    subdata, temp = readPacket(submsg[j:], single=True)
                    j += temp
                    data.extend(subdata)
                i += length
                op = 0
                
            else:
                subpkts = int(msg[i+1:i+12], base=2)
                i += 12
                for _ in range(0,subpkts):
                    subdata, temp = readPacket(msg[i:], single=True)
                    i += temp
                    data.extend(subdata)
                op = 1

        pkts.append(Packet(ver, typ, data, opType=op))
        if single:
            break
    return pkts, i

with open("input.txt") as file:
    line = file.readline().strip()
    msg = ''
    for char in line:
        msg += format(int(char, base=16), '04b')

    packets, _ = readPacket(msg)
    
    val = packets[0].getValue()
    print(val)