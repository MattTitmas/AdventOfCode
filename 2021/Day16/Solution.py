from aoc import get_input
from utils import function_timer_avg, function_timer


import math
@function_timer_avg
def part1(data):
    values = data
    binary = str(bin(int(values, 16)))[2:].zfill(len(values) * 4)
    def analyzePacket(packet: str):
        totalPacketNo = int(packet[0:3], 2)
        typeID = int(packet[3:6], 2)
        if typeID != 4:
            lengthTypeID = int(packet[6:7], 2)
            if lengthTypeID == 1:
                totalLength = 18
                numberOfSubPackets = int(packet[7:18], 2)
                numberOfSubPacketsRead = 0
                startingBit = 18
                while numberOfSubPacketsRead < numberOfSubPackets:
                    lenOfSubPacket, pack = analyzePacket(packet[startingBit:])
                    totalPacketNo += pack
                    startingBit += lenOfSubPacket
                    numberOfSubPacketsRead += 1
                    totalLength += lenOfSubPacket
            else:
                totalLength = 22
                lengthOfSubPackets = int(packet[7:22], 2)
                numberOfBitsUsed = 0
                startingBit = 22
                while numberOfBitsUsed < lengthOfSubPackets:
                    lenOfSubPacket, pack = analyzePacket(packet[startingBit:])
                    totalPacketNo += pack
                    startingBit += lenOfSubPacket
                    numberOfBitsUsed += lenOfSubPacket
                    totalLength += lenOfSubPacket
        else:
            # TypeID = 4 : Literal value
            stop = False
            currentBit = 6
            totalBin = ""
            while not stop:
                val = packet[currentBit:currentBit + 5]
                stop = (True if val[0] == '0' else False)
                totalBin += val[1:5]
                currentBit += 5
            return 6 + len(totalBin) + len(totalBin) // 4, totalPacketNo
        return totalLength, totalPacketNo

    return analyzePacket(binary)[1]


@function_timer_avg
def part2(data):
    values = data
    binary = str(bin(int(values, 16)))[2:].zfill(len(values) * 4)

    def analyzePacket(packet: str):
        commands = {
            0: sum,
            1: math.prod,
            2: min,
            3: max,
            5: (lambda vals: 1 if vals[0] > vals[1] else 0),
            6: (lambda vals: 1 if vals[0] < vals[1] else 0),
            7: (lambda vals: 1 if vals[0] == vals[1] else 0)
        }
        totalValue = []
        typeID = int(packet[3:6], 2)
        if typeID != 4:
            lengthTypeID = int(packet[6:7], 2)
            if lengthTypeID == 1:
                totalLength = 18
                numberOfSubPackets = int(packet[7:18], 2)
                numberOfSubPacketsRead = 0
                startingBit = 18
                while numberOfSubPacketsRead < numberOfSubPackets:
                    lenOfSubPacket, value = analyzePacket(packet[startingBit:])
                    totalValue.append(value)
                    startingBit += lenOfSubPacket
                    numberOfSubPacketsRead += 1
                    totalLength += lenOfSubPacket
            else:
                totalLength = 22
                lengthOfSubPackets = int(packet[7:22], 2)
                numberOfBitsUsed = 0
                startingBit = 22
                while numberOfBitsUsed < lengthOfSubPackets:
                    lenOfSubPacket, value = analyzePacket(packet[startingBit:])
                    totalValue.append(value)
                    startingBit += lenOfSubPacket
                    numberOfBitsUsed += lenOfSubPacket
                    totalLength += lenOfSubPacket
        else:
            # TypeID = 4 : Literal value
            stop = False
            currentBit = 6
            totalBin = ""
            while not stop:
                val = packet[currentBit:currentBit + 5]
                stop = (True if val[0] == '0' else False)
                totalBin += val[1:5]
                currentBit += 5
            return 6 + len(totalBin) + len(totalBin) // 4, int(totalBin, 2)
        valueToReturn = commands[typeID](totalValue)
        return totalLength, valueToReturn

    return analyzePacket(binary)[1]

def main():
    data = get_input(16, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
