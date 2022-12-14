from typing import Dict


class IntCode:
    def __init__(self, data: str, given_inputs=[]) -> None:
        self.commands = list(map(int, data.split(',')))
        self.instruction_pointer = 0
        self.inputs = given_inputs
        self.input_var = 0

    parameters = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3
    }

    outputs = []

    def opcode_one(self, values):
        self.commands[values[2]] = values[1] + values[0]
        return self.parameters[1] + 1

    def opcode_two(self, values):
        self.commands[values[2]] = values[1] * values[0]
        return self.parameters[2] + 1

    def opcode_three(self, values):
        if self.input_var < len(self.inputs):
            self.commands[values[0]] = self.inputs[self.input_var]
            self.input_var += 1
        else:
            val = int(input('Please input a value:\n'))
            self.commands[values[0]] = val
        return self.parameters[3] + 1

    def opcode_four(self, values):
        print(values[0])
        self.outputs.append(values[0])
        return self.parameters[4] + 1

    def opcode_five(self, values):
        if values[0] == 0:
            return self.parameters[5] + 1
        return values[1] - self.instruction_pointer

    def opcode_six(self, values):
        if values[0] != 0:
            return self.parameters[6] + 1
        return values[1] - self.instruction_pointer

    def opcode_seven(self, values):
        self.commands[values[2]] = 1 if values[0] < values[1] else 0
        return self.parameters[7] + 1

    def opcode_eight(self, values):
        self.commands[values[2]] = 1 if values[0] == values[1] else 0
        return self.parameters[8] + 1

    functions = {
        1: opcode_one,
        2: opcode_two,
        3: opcode_three,
        4: opcode_four,
        5: opcode_five,
        6: opcode_six,
        7: opcode_seven,
        8: opcode_eight
    }

    write_to = {
        1,
        2,
        3,
        7,
        8
    }

    def get_parameter_values(self, modes: Dict[int, int], current_instruction) -> Dict[int, int]:
        keys = list(modes.keys())
        to_return = dict()
        for count, param in enumerate(keys, start=1):
            mode = modes[param]
            if current_instruction % 100 in self.write_to and param == keys[-1]:
                to_return[param] = self.commands[self.instruction_pointer + count]
            elif mode == 1:
                to_return[param] = self.commands[self.instruction_pointer + count]
            else:
                to_return[param] = self.commands[self.commands[self.instruction_pointer + count]]
        return to_return

    def run_instruction(self) -> int:
        # Fetch
        current_instruction = self.commands[self.instruction_pointer]

        # Decode
        number_of_parameters = self.parameters[current_instruction % 100]
        modes = dict()
        for i in range(number_of_parameters):
            # (i + 2) to account for the 2 right-most being the instruction
            modes[i] = (current_instruction // (10 ** (i + 2))) % 10
        values = self.get_parameter_values(modes, current_instruction)

        # Execute
        return self.functions[current_instruction % 100](self, values)


    def run_program(self) -> None:
        while self.commands[self.instruction_pointer] != 99:
            val = self.run_instruction()
            self.instruction_pointer += val
