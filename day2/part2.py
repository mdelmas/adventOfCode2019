from itertools import product


def runIntcodeProgram(program, noun, verb):
    program[1] = noun
    program[2] = verb
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break
        posVal1 = program[i+1]
        posVal2 = program[i+2]
        posRes = program[i+3]
        if opcode == 1:
            program[posRes] = program[posVal1] + program[posVal2]
        elif opcode == 2:
            program[posRes] = program[posVal1] * program[posVal2]
    return program[0]


for noun, verb in product(range(1, 100), range(1, 100)):
    program = [int(x) for x in open("./input").readlines()[0].split(',')]
    result = runIntcodeProgram(program, noun, verb)
    print(result)
    if result == 19690720:
        break


print("noun = " + str(noun))
print("verb = " + str(verb))
print("100 * noun + verb = " + str(100*noun + verb))
