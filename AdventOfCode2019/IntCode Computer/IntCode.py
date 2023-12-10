class intCodeVM:
    def __init__(self, inp: str):
        self.__input = inp
        self.__instructionList = [int(i) for i in open(inp).read().split(",")]
        self.__programCounter = 0
        self.__correspondingInputs = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            99: 0,
        }

        def add(inp):
            self.__instructionList[inp[2]] = inp[0] + inp[1]

        def multiply(inp):
            self.__instructionList[inp[2]] = inp[0] * inp[1]

        def takeInput(inp):
            self.__instructionList[inp[0]] = int(input("Please give an input:\n"))

        def output(inp):
            if inp[1] != "lit":
                print(self.__instructionList[inp[0]])
            else:
                print(inp[0])

        def jump_if_true(inp):
            if inp[0] != 0:
                self.__programCounter = inp[1]

        def jump_if_false(inp):
            if inp[0] == 0:
                self.__programCounter = inp[1]

        def less_than(inp):
            self.__instructionList[inp[2]] = 1 if inp[0] < inp[1] else 0

        def equals(inp):
            self.__instructionList[inp[2]] = 1 if inp[0] == inp[1] else 0

        def halt(inp):
            self.__finished = True
            return

        self.__correspondingFunctions = {
            1: add,
            2: multiply,
            3: takeInput,
            4: output,
            5: jump_if_true,
            6: jump_if_false,
            7: less_than,
            8: equals,
            99: halt,
        }

    def getInstructions(self):
        return self.__instructionList

    def executeCurrentInstruction(self):
        instruction = str(self.__instructionList[self.__programCounter])
        while len(instruction) != 5:
            instruction = "0" + instruction

        addressingModes = instruction[0:-2]
        opcode = int(instruction[-2:])

        noInputs = self.__correspondingInputs[opcode]
        self.__programCounter += 1
        inp = []
        for i in range(noInputs):
            mode = int(addressingModes[-(i + 1)])
            if mode == 0:
                if i == noInputs - 1:
                    inp.append(self.__instructionList[self.__programCounter])
                else:
                    inp.append(
                        self.__instructionList[
                            self.__instructionList[self.__programCounter]
                        ]
                    )
                if opcode == 4:
                    inp.append("pos")
            else:
                inp.append(self.__instructionList[self.__programCounter])
                if opcode == 4:
                    inp.append("lit")
            self.__programCounter += 1

        print(opcode, inp)
        self.__correspondingFunctions[opcode](inp)

    def executeUntilEnd(self):
        self.__finished, self.__error = False, False
        while not self.__finished and not self.__error:
            self.executeCurrentInstruction()

    def getLocation(self, n: int):
        return self.__instructionList[n]

    def replaceInstruction(self, pos: int, newVal: int):
        self.__instructionList[pos] = newVal

    def reset(self):
        self.__init__(self.__input)


comp = intCodeVM("input2.txt")
# comp.replaceInstruction(1, 12); comp.replaceInstruction(2, 2)
comp.executeUntilEnd()
# print(comp.getLocation(0))
comp.reset()
