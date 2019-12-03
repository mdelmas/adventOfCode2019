def runIntcodeProgram(program):
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

program = [int(x) for x in open("./input").readlines()[0].split(',')]
program[1] = 12
program[2] = 2
result = runIntcodeProgram(program)
print("Value at position 0 after program halts = " + str(result))