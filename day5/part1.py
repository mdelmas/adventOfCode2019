def runIntcodeProgram(program):
    i = 0
    while i < len(program):
        opcode = program[i]
        if opcode == 99:
            break
        if opcode == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            i += 4
        elif opcode == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
            i += 4
        elif opcode == 3:
            program[program[i+1]] = int(input())
            i += 2
        elif opcode == 4:
            print(program[program[i+1]])
            i += 2
    return program[0]

program = [int(x) for x in open("./test").readlines()[0].split(',')]
result = runIntcodeProgram(program)
print("Value at position 0 after program halts = " + str(result))