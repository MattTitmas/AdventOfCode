def part1():
    values = [(i.split(" => ")[0],i.split(" => ")[1]) for i in open("input.txt","r").read().split("\n\n")[0].split("\n")]
    replacements = dict()
    for molecule, replacement in values:
        replacements[molecule] = [replacement] if molecule not in replacements else replacements[molecule] + [replacement]
    molecule = open("input.txt","r").read().split("\n\n")[1]
    newMolecules = set()
    currentMol = molecule[0]
    for count, char in enumerate(molecule[1:]):
        if char.upper() == char:
            if currentMol in replacements:
                for replaceable in replacements[currentMol]:
                    newMolecules.add(molecule[:count - len(currentMol) + 1] + replaceable + molecule[count + 1:])
            currentMol = char
        else:
            currentMol += char

    if currentMol in replacements:
        for replaceable in replacements[currentMol]:
            newMolecules.add(molecule[:len(molecule) - len(currentMol)] + replaceable)
    return len(newMolecules)

def part2():
    import re
    molecule = open("input.txt","r").read().split('\n')[-1][::-1]
    reps = {m[1][::-1]: m[0][::-1]
            for m in re.findall(r'(\w+) => (\w+)', open("input.txt","r").read())}

    def rep(x):
        return reps[x.group()]

    count = 0
    while molecule != 'e':
        molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
        count += 1
    return count

print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
